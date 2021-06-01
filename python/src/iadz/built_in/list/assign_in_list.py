# -*- coding: utf-8 -*-


def foo():

    bar = None

    for i in range(5):

        if i == 3:
            bar = 3

    if not bar:
        print("bar is None")
    else:
        print("bar is assigned unexpectedly!!")


if __name__ == "__main__":
    foo()
