# -*- coding: utf-8 -*-
import pycountry
from enum import Enum

CurrencyCodeType = Enum(
    "CurrencyCodeType",
    [(currency.alpha_3, currency.alpha_3) for currency in pycountry.currencies],
)

if __name__ == "__main__":
    print(CurrencyCodeType.GBP)
