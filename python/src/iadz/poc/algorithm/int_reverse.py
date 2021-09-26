# -*- coding: utf-8 -*-


def int_reverse(x):

    a = 0
    lst = []
    if x > 0:
        for i in range(1, 33):
            lst.insert(i, x % (10 ** i) // 10 ** (i - 1))
            if x // (10 ** i) == 0:
                break

        lst = list(reversed(lst))

        k = 1
        for j in lst:
            a = j * (10 ** (k - 1)) + a
            k += 1
        if -(2 ** 31) < a < 2 ** 31 - 1:
            return a
        else:
            return 0
    elif x < 0:
        x = x * -1

        for i in range(1, 33):
            lst.insert(i, x % (10 ** i) // 10 ** (i - 1))
            if x // (10 ** i) == 0:
                break

        lst = list(reversed(lst))

        k = 1
        for j in lst:
            a = j * (10 ** (k - 1)) + a
            k += 1
        if -(2 ** 31) < a < 2 ** 31 - 1:
            return -a
        else:
            return 0

    else:
        return 0


def reverse(x):

    y, res = abs(x), 0
    of = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > of:
            return 0
        y //= 10
    return res if x > 0 else -res


if __name__ == "__main__":
    print(int_reverse(-321))
