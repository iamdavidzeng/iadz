# -*- coding: utf-8 -*-

from decimal import Decimal


class Foo:

    first_amount = None
    second_amount = None


def generate_data(foo: Foo, data: dict):
    """
    Update different amount according to foo.x_amount and type,
    Use dict get function to calculate instead of if/else statements.

    Args:
        foo: old Foo
        data:
            {
                "type": "plus",
                "amount": Decimal(100),
                ...
            }

    Returns:
        updated data
    """
    first_amount = foo.first_amount or 0
    second_amount = foo.second_amount or 0
    type_ = data.get("type")
    amount = data.get("amount")
    update_data = {}
    calculator = {
        "plus": lambda: update_data.update(**{"first_amount": first_amount + amount}),
        "minus": lambda: update_data.update(
            **{"second_amount": second_amount - amount}
        ),
        "plus_and_minus": lambda: update_data.update(
            **{
                "first_amount": first_amount + amount,
                "second_amount": second_amount - amount,
            }
        ),
    }

    calculator[type_]()

    data.update(**update_data)
    return data


if __name__ == "__main__":

    foo = Foo()
    data = {"type": "plus_and_minus", "amount": Decimal(100)}

    print(f"{generate_data(foo, data)}")
