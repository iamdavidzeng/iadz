# -*- coding: utf-8 -*-

from enum import Enum


class FooEnum(Enum):
    FOO = "foo"
    BAR = "bar"

    BAZ = "baz"


class BarEnum(Enum):
    FOO = "foo"
    BAR = "bar"

    FIZ = "fiz"


class BazEnum:
    pass



print(BazEnum.FOO)
