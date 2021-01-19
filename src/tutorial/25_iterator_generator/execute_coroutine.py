# -*- coding: utf-8 -*-


def print_name(prefix):

    print(f"Searching prefix: {prefix}")

    try:

        while True:
            name = yield
            if prefix in name:
                print(name)
    except GeneratorExit:
        print(f"Closing coroutine!")


if __name__ == "__main__":

    co = print_name("Dear")

    co.__next__()

    co.send("Foo")
    co.send("Dear Foo")

    co.close()
