# -*- coding: utf-8 -*-
from enum import Enum
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
the_day_before_yesterday = yesterday - timedelta(days=1)


class Category(Enum):
    @property
    def flow(self):
        return {}  # pragma: no cover

    @property
    def expanded_flow(self):
        return self.flow

    def __gt__(self, previous):
        allowed_next = self.expanded_flow.get(previous) or []
        return self in allowed_next

    def __lt__(self, next_):
        allowed_next = self.expanded_flow.get(self) or []
        return next_ in allowed_next

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return self.value


class TransactionCategory(Category):

    RENT = "rent"
    DAMAGE = "damage"
    ADDITIONAL_FEE = "additional_fee"
    OTHER = "other"

    @property
    def flow(self):
        return {
            self.DAMAGE: [self.RENT, self.ADDITIONAL_FEE, self.OTHER],
            self.RENT: [self.ADDITIONAL_FEE, self.OTHER],
            self.ADDITIONAL_FEE: [self.OTHER],
            self.OTHER: None,
        }


lst = [
    {
        "id": 1,
        "invoice_datetime": today,
        "created_at": yesterday,
        "category": TransactionCategory.RENT,
    },
    {
        "id": 2,
        "invoice_datetime": today,
        "created_at": yesterday,
        "category": TransactionCategory.OTHER,
    },
    {
        "id": 3,
        "invoice_datetime": yesterday,
        "created_at": yesterday,
        "category": TransactionCategory.RENT,
    },
    {
        "id": 4,
        "invoice_datetime": yesterday,
        "created_at": the_day_before_yesterday,
        "category": TransactionCategory.DAMAGE,
    },
    {
        "id": 5,
        "invoice_datetime": yesterday,
        "created_at": the_day_before_yesterday,
        "category": TransactionCategory.OTHER,
    },
]


def compare_item_in_lst(lst):
    def sorter(item):

        return (item["invoice_datetime"], item["created_at"], item["category"])

    return sorted(lst, key=sorter)


if __name__ == "__main__":
    result = compare_item_in_lst(lst)
    print(result)
