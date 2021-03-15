# -*- coding: utf-8 -*-


from collections import defaultdict

import pytest

from nameko.extensions import DependencyProvider
from nameko.events import EventDispatcher, event_handler
from nameko.exceptions import RemoteError
from nameko.rpc import rpc, RpcProxy
from nameko.standalone.rpc import ServiceProxy
from nameko.testing.services import replace_dependencies, restrict_entrypoints
from nameko.testing.utils import get_container
from nameko.timer import timer


class NotLoggedInError(Exception):
    pass


class ItemOutOfStockError(Exception):
    pass


class ItemDoesNotExistError(Exception):
    pass


class ShoppingBasket(DependencyProvider):
    def __init__(self):
        self.baskets = defaultdict(list)

    def get_dependency(self, worker_ctx):
        class Basket(object):
            def __init__(self, basket):
                self._basket = basket
                self.worker_ctx = worker_ctx

            def add(self, item):
                self._basket.append(item)

            def __iter__(self):
                for item in self._basket:
                    yield item

        try:
            user_id = worker_ctx.data["user_id"]
        except KeyError:
            raise NotLoggedInError
        return Basket(self.baskets[user_id])


class AcmeShopService:

    name = "acmeshopservice"

    user_basket = ShoppingBasket()
    stock_rpc = RpcProxy("stockservice")
    invoice_rpc = RpcProxy("invoiceservice")
    payment_rpc = RpcProxy("paymentservice")

    fire_event = EventDispatcher()

    @rpc
    def add_to_basket(self, item_code):
        stock_level = self.stock_rpc.check_stock(item_code)
        if stock_level > 0:
            self.user_basket.add(item_code)
            self.fire_event("item_add_to_basket", item_code)
            return item_code

        raise ItemOutOfStockError(item_code)

    @rpc
    def checkout(self):
        total_price = sum(self.stock_rpc.check_price(item) for item in self.user_basket)

        invoice = self.invoice_rpc.prepare_invoice(total_price)

        self.payment_rpc.take_payment(invoice)

        checkout_event_data = {"invoice": invoice, "items": list(self.user_basket)}

        self.fire_event("checkout_complete", checkout_event_data)

        return total_price


class WareHouse(DependencyProvider):
    def __init__(self):
        self.database = {
            "anvil": {"price": 100, "stock": 3},
            "dehydrated_boulders": {
                "price": 999,
                "stock": 12,
            },
            "invisible_paint": {
                "price": 10,
                "stock": 30,
            },
            "toothpicks": {
                "price": 1,
                "stock": 0,
            },
        }

    def get_dependency(self, worker_ctx):
        return self.database


class StockService:

    name = "stockservice"

    warehouse = WareHouse()

    @rpc
    def check_price(self, item_code):
        try:
            return self.warehouse[item_code]["price"]
        except KeyError:
            raise ItemDoesNotExistError(item_code)

    @rpc
    def check_stock(self, item_code):
        try:
            return self.warehouse[item_code]["stock"]
        except KeyError:
            raise ItemDoesNotExistError(item_code)

    @rpc
    @timer(100)
    def monitor_stock(self):
        raise NotImplementedError()

    @event_handler("acmesshopservice", "checkout_complete")
    def dispatch_items(self, event_data):
        raise NotImplementedError


class AddressBook(DependencyProvider):
    def __init__(self):
        self.address_book = {
            "wile_e_coyote": {
                "username": "wile_e_coyote",
                "fullname": "wile E Coyote",
                "address": "12 Long Road, High Cliffs, Utah",
            },
        }

    def get_dependency(self, worker_ctx):
        def get_user_details():
            try:
                user_id = worker_ctx.data["user_id"]
            except KeyError:
                raise NotLoggedInError()
            return self.address_book.get(user_id)

        return get_user_details


class InvoiceService:

    name = "invoceservice"

    get_user_details = AddressBook()

    @rpc
    def prepare_invoice(self, amount):

        address = self.get_user_details().get("address")
        fullname = self.get_user_details().get("fullname")
        username = self.get_user_details().get("username")

        msg = "Dear {}. Please pay ${} to ACME Corp.".format(fullname, amount)

        invoice = {
            "message": msg,
            "amount": amount,
            "customer": username,
            "address": address,
        }
        return invoice


class PaymentService:

    name = "paymentservice"

    @rpc
    def take_payment(self, invoice):
        raise NotImplementedError()


# ============================
# begin test
# ============================


@pytest.yield_fixture()
def rpc_proxy_factory(rabbit_config):

    all_proxies = []

    def make_proxy(service_name, **kwargs):
        proxy = ServiceProxy(service_name, rabbit_config, **kwargs)
        all_proxies.append(proxy)
        return proxy.start()

    yield make_proxy

    for proxy in all_proxies:
        proxy.stop()


def test_shop_checkout_integration(rabbit_config, runner_factory, rpc_proxy_factory):
    context_data = {"user_id": "wile_e_coyote"}

    shop = rpc_proxy_factory("acmesshopservice", context_data=context_data)

    runner = runner_factory(
        rabbit_config, AcmeShopService, StockService, InvoiceService
    )

    shop_container = get_container(runner, AcmeShopService)
    fire_event, payment_rpc = replace_dependencies(
        shop_container, "fire_event", "payment_rpc"
    )

    stock_container = get_container(runner, StockService)
    restrict_entrypoints(stock_container, "check_price", "check_stock")

    runner.start()

    assert shop.add_to_basket("anvil") == "anvil"
    assert shop.add_to_basket("invisible_paint") == "invisible_paint"

    with pytest.raises(RemoteError) as exc_info:
        shop.add_to_basket("toothpicks")
    assert exc_info.value.exc_type == "ItemOutOfStockError"

    payment_rpc.take_payment.return_value = "Payment complete."

    res = shop.checkout()

    total_amount = 100 + 10
    assert res == total_amount

    payment_rpc.take_payment.assert_called_once_with(
        {
            "customer": "wile_e_coyote",
            "address": "12 Long Road, High Cliffs, Utah",
            "amount": total_amount,
            "message": "Dear Wile E Coyote, Please pay $110 to ACME Corp.",
        }
    )

    assert fire_event.call_count == 3
