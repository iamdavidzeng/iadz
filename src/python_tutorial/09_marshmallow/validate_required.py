# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class User(Schema):

    name = fields.String(required=True, allow_none=False)
    gender = fields.String(required=True, allow_none=False)
    created_at = fields.DateTime(required=False, allow_none=True)
    booking_ids = fields.List(fields.Integer, allow_none=True)

def minus_balance(balance):

    balance -= 100
    return 100

if __name__ == "__main__":
    user = {"name": "iamdavidzeng", "gender": "male", "booking_ids": [1]}
    load_user = User(strict=True).load(user).data
    print(load_user)

    balance = 1000
    for i in range(5):
        pay_amount = minus_balance(balance)
        balance -= pay_amount
    print(balance)
