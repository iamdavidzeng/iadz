# -*- coding: utf-8 -*-

from decimal import Decimal

from iadz.built_in.dict.use_dict_replace_if_else import Foo


def generate_data(foo: Foo, data: dict) -> dict:
    """
    The same functionality of func in dict
    """

    first_amount = foo.first_amount or 0
    second_amount = foo.second_amount or 0
    type_ = data.get("type")
    amount = data.get("amount")

    increase_first_amount = ["plus", "plus_and_minus"]
    decrease_second_amount = ["minus", "plus_and_minus"]

    if type_ in increase_first_amount:
        first_amount += amount

    if type_ in decrease_second_amount:
        second_amount -= amount

    data.update(first_amount=first_amount, second_amount=second_amount)
    return data


if __name__ == "__main__":

    foo = Foo()
    data = {"type": "plus_and_minus", "amount": Decimal(100)}

    print(f"{generate_data(foo, data)}")
