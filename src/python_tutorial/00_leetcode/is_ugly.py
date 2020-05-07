# -*- coding: utf-8 -*-


def is_ugly(num):
    if num <= 0:
        return False

    for n in (2, 3, 5):
        while num % n == 0:
            num //= n

    return num == 1


if __name__ == "__main__":
    print(is_ugly(1))
