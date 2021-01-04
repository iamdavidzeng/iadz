# -*- coding: utf-8 -*-

from decimal import Decimal

payment_items = [
    {"total_amount": Decimal(200), "paid_amount": None},
    {"total_amount": Decimal(100), "paid_amount": Decimal(50)},
]


total_amount = sum(
    [
        pi["total_amount"] - pi["paid_amount"]
        if pi["paid_amount"]
        else pi["total_amount"]
        for pi in payment_items
    ]
)
print(f"total_amount: {total_amount}")
