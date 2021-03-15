# -*- coding: utf-8 -*-

from collections import defaultdict

payment_items = [
    {
        "id": 1,
        "description": "Deposit",
        "paid_amount": 500,
        "currency": "GBP",
        "student_id": 1,
        "status": "paid",
    },
    {
        "id": 2,
        "description": "1st Installment",
        "paid_amount": 1000,
        "currency": "GBP",
        "student_id": 1,
        "status": "paid",
    },
    {
        "id": 3,
        "description": "2nd Installment",
        "paid_amount": 1000,
        "currency": "GBP",
        "student_id": 1,
        "status": "invoiced",
    },
    {
        "id": 4,
        "description": "3rd Installment",
        "paid_amount": 1000,
        "currency": "GBP",
        "student_id": 1,
        "status": "invoiced",
    },
    {
        "id": 5,
        "description": "Admin Fee",
        "paid_amount": 100,
        "currency": "GBP",
        "student_id": 1,
        "status": "overdue",
    },
]

student_ids = set(map(lambda x: x["student_id"], payment_items))

students = {
    student_id: {"paid": [], "invoiced": [], "overdue": []}
    for student_id in student_ids
}


for pi in payment_items:
    if pi["status"] in students[pi["student_id"]].keys():
        students[pi["student_id"]][pi["status"]].append(pi)


payload_lst = [
    {"student_id": key, "payment_items": value} for key, value in students.items()
]


if __name__ == "__main__":

    print(payload_lst)
