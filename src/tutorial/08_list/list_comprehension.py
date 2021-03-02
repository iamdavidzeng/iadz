# -*- coding: utf-8 -*-

from decimal import Decimal


def make_payment_item(**overrides):
    data = {
        "id": 1,
        "paid_amount": Decimal(100),
        "total_amount": Decimal(100),
        "status": "paid",
    }
    data.update(**overrides)
    return data


def pop_duplicated_payment_items():

    foo = [
        make_payment_item(id=1, paid_amount=Decimal(0), status="open"),
        make_payment_item(id=1, paid_amount=Decimal(50), status="remaining"),
        make_payment_item(id=2),
    ]

    payment_item = make_payment_item(id=1)

    bar = [p for p in foo if p["id"] != payment_item["id"]]

    bar.append(payment_item)

    return bar


if __name__ == "__main__":
    print(f"payment_items: {pop_duplicated_payment_items()}")
