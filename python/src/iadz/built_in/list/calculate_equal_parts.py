# -*- coding: utf-8 -*-

from decimal import Decimal

total = 100

number = 3


previous_plans = [
    {"value": Decimal(100 / 3).quantize(Decimal(".000001"))} for i in range(1, 3)
]

last_plan = {"value": Decimal(100) - sum([p["value"] for p in previous_plans])}

plans = [*previous_plans, last_plan]


print(f"plans: {plans}")
