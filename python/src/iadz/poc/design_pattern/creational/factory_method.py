from __future__ import annotations


class Factory:
    def factory_method(self):
        raise NotImplementedError


class SquareFactory:
    def factory_method(self):
        return Square()


class Square:
    def create(self):
        print("square")


def main():
    """
    >>> shape = SquareFactory().factory_method().create()
    square
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
