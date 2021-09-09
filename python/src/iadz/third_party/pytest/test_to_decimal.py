import pytest
from typing import Union
from decimal import Decimal


def to_decimal(value: Union[int, str, float, Decimal]) -> Decimal:
    return Decimal(str(value)) if value else Decimal("0.00")


@pytest.mark.parametrize(
    ["args", "expected"],
    [
        ({"value": 100.11}, Decimal("100.11")),
        ({"value": "100.11"}, Decimal("100.11")),
        ({"value": 100.11}, Decimal("100.11")),
        ({"value": Decimal("100.11")}, Decimal("100.11")),
        ({"value": None}, Decimal("0.00")),
    ],
)
def test_to_decimal(args, expected):
    assert expected == to_decimal(args["value"])
