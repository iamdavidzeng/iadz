"""
Implementation of the iterator pattern with a generator
"""


def count_to(count):
    numbers = ["one", "two", "three", "four", "five"]
    yield from numbers[:count]


def main():
    """
    # Counting to two...
    >>> for number in count_to(2):
    ...     print(number)
    one
    two

    # Counting to five...
    >>> for number in count_to(5):
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()