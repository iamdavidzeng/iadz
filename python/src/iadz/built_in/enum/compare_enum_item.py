# -*- coding: utf-8 -*-
from enum import Enum
from collections import defaultdict


class Category(Enum):
    @property
    def flow(self):
        return {}  # pragma: no cover

    @property
    def expanded_flow(self):
        if not hasattr(self, "_expanded_flow"):
            self.__expanded_flow = _expand(self.flow)
        return self.__expanded_flow

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


def _expand(flow):

    arcs = [
        (previous, next_)
        for previous, allowed_next in flow.items()
        for next_ in allowed_next or [None]
    ]

    def collect(parent):
        for previous, next_ in arcs:
            if previous == parent and next_:
                yield next_
                for child in collect(next_):
                    yield child

    expanded = defaultdict(set)
    for previous, next_ in arcs:
        for child in collect(previous):
            expanded[previous].add(child)

    return expanded


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


if __name__ == "__main__":
    categorys = [
        TransactionCategory.DAMAGE,
        TransactionCategory.OTHER,
        TransactionCategory.RENT,
        TransactionCategory.DAMAGE,
        TransactionCategory.ADDITIONAL_FEE,
    ]
    print(sorted(categorys))
