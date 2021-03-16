# -*- coding: utf-8 -*-


import inspect


class Foo:

    pass


def bar(id_, data, commit=True):
    pass


if __name__ == "__main__":
    foo = Foo()
    module = inspect.getmodule(foo)
    print(f"{module.__name__}.{type(foo).__name__}")

    callargs = inspect.getcallargs(bar, 1, {})
    print(f"{callargs}")

    signature = inspect.signature(bar)
    default_args = {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
    print(f"{default_args}")
