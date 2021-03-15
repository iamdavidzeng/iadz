# -*- coding: utf-8 -*-

import inspect


def func1(name, gender="male", *args, **kwargs):
    pass


if __name__ == "__main__":
    signature = inspect.signature(func1)

    for k, v in signature.parameters.items():
        print(f"param_name: {k}, deafault_value: {v.default}")
