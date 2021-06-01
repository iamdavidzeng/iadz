# -*- coding: utf-8 -*-


def foo(name, **kwargs):
    bar(**kwargs, name=name)


def bar(**kwargs):
    print(kwargs)


if __name__ == "__main__":

    foo("david", gender="male")
