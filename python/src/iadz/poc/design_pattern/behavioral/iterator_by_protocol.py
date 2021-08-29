"""
Implementation of the iterator pattern using the iterator protocol from Python
"""


class NumberWords:

    WORDS = ("one", "two", "three", "four", "five")

    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop or self.start > len(self.WORDS):
            raise StopIteration
        current = self.start
        self.start += 1
        return self.WORDS[current - 1]


def main():
    """
    # Counting to two...
    >>> for number in NumberWords(start=1, stop=2):
    ...     print(number)
    one
    two

    # Counting to five...
    >>> for number in NumberWords(start=1, stop=5):
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
