# -*- coding: utf-8 -*-
from decimal import Decimal

from marshmallow import Schema
from marshmallow.fields import Decimal as DecimalField


class BalanceSchema(Schema):
    wallet_balance = DecimalField(2, required=True, allow_none=False, as_string=True)
    credit_balance = DecimalField(2, required=True, allow_none=True, as_string=True)


if __name__ == "__main__":

    data = {"wallet_balance": 100.22, "credit_balance": None}

    print(Decimal(100.22))

    loaded_balance = BalanceSchema(strict=True).load(data).data
    print(f"after load: {loaded_balance}")

    dumped_balance = BalanceSchema().dump(data).data
    print(f"after dump: {dumped_balance}")
