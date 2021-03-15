# -*- coding: utf-8 -*-

from enum import Enum


class FinancialStatus(Enum):

    IN_BALANCE = "in_balance"
    """
    Means current_balance equals to 0
    """

    IN_ARREARS = "in_arrears"
    """
    Means the current_balance is a negative number
    """

    IN_CREDIT = "in_credit"
    """
    Means the current_balance is a positive number
    """


example_dict = {"name": "iamdavidzeng", "status": FinancialStatus.IN_ARREARS}


for key, value in example_dict.items():

    print(type(value))

    if isinstance(value, Enum):
        example_dict[key] = value.value


if __name__ == "__main__":

    print(example_dict)

