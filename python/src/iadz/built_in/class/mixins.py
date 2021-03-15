# -*- coding: utf-8 -*-

import logging

from decimal import Decimal
from collections import defaultdict


logger = logging.getLogger(__name__)


class PaymentItem:
    pass


class PaymentItemSchema:
    pass


class Storage:
    pass


class NotFound(Exception):
    pass


class EntityNotFound(Exception):
    pass


class PaymentItemBase:

    payment_item_autocrud = None

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def _create_payment_item(self, data: dict, commit: bool = True) -> PaymentItem:
        """
        Internal method to create PaymentItem

        Args:
            data:
                {
                    ...
                }

        Returns:
            {
                ...
            }
        """
        payment_item = self.storage.payment_items.create(data, commit=commit)
        self._dispatch_event(
            "payment_item_created",
            {"data": PaymentItemSchema(strict=True).dump(payment_item).data},
            direct=commit,
        )

        return payment_item

    def _update_payment_item(
        self, id_: int, data: dict, commit: bool = True
    ) -> PaymentItem:
        """
        Internal method to update PaymentItem

        Args:
            id_: id of the PaymentItem
            data:
                {
                    ...
                }
            commit=True: determine whether to commit or not

        Returns:
            {
                ...
            }
        """
        try:
            payment_item = self.storage.payment_items.update(id_, data, commit=commit)
        except NotFound:
            raise EntityNotFound(f"")
        else:
            self._dispatch_event(
                "payment_item_created",
                {"data": PaymentItemSchema(strict=True).dump(payment_item).data},
                direct=commit,
            )
            return payment_item

    def create_payment_item(self, data: dict) -> dict:
        """
        Create PaymentItem
        Args:
            data:
                {
                    "description": "rental",
                    ...
                }

        Returns:
            {
                "id": 1,
                "description": "rental",
                ...
            }
        """
        payment_item = self._create_payment_item(data, commit=False)
        return PaymentItemSchema(strict=True).dump(payment_item).data

    def update_payment_item(self, data: dict) -> dict:
        id_ = data.pop("id")

        payment_item = self._update_payment_item(id_, data, commit=False)

        return PaymentItemSchema(strict=True).dump(payment_item).data

    def remove_payment_item(self, id_: int) -> dict:
        pass


class PaymentItemCronjob:
    def invoice_or_charge_payment_items(self):
        pass

    def trigger_automatic_payment_for_payment_items(self):
        pass


class PaymentItemEvent:
    event_mappings = defaultdict(list)

    def _dispatch_event(self, event_name: str, payload: dict, direct=True):
        """
        Dispatch PaymentItem's events to corresponding event handlers.

        Args:
            event_name: declare a signal for event handler
            payload:
                {
                    "id": 1,
                    ...
                }
            direct=True: determine whether to dispatch synchronously or asynchronously

        Returns:
        """
        if direct:
            self.event_dispatcher(event_name, payload)
        else:
            event = (event_name, payload)
            self.event_mappings[str(id(self))].append(event)


class PaymentItemMixin(PaymentItemBase, PaymentItemCronjob, PaymentItemEvent):
    pass


if __name__ == "__main__":

    service = PaymentItemMixin(None)
    data = {
        "description": "mock_description",
        "amount": Decimal(100),
    }
    service.create_payment_item(data)
