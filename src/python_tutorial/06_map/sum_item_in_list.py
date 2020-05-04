# -*- coding: utf-8 -*-


lst = [
    {"total_amount": 100, "paid_amount": 50},
    {"total_amount": 100, "paid_amount": 50},
    {"total_amount": 100, "paid_amount": 50},
    {"total_amount": 100, "paid_amount": None},
]

if __name__ == "__main__":
    total_amount = sum(map(lambda x: x["total_amount"], lst))
    paid_amount = sum(map(lambda x: x["paid_amount"] if x["paid_amount"] else 0, lst))
    print(total_amount)
    print(paid_amount)

    total_balance = total_amount - paid_amount
    print(total_balance)
