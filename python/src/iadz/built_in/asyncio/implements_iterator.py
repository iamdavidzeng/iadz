# -*- coding: utf-8 -*-


class Foo:
    def __init__(self, values: list) -> None:
        super().__init__()
        self.values = values

    def __iter__(self):
        return self

    def __next__(self):

        if self.values:
            return self.values.pop()

        raise StopIteration()


if __name__ == "__main__":

    foo = Foo([1, 2, 3])

    for i in range(4):
        print(next(foo))
