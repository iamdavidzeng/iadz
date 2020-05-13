#  -*- coding: utf-8 -*-


def add_digits(num):
    if num < 10:
        return num
    else:
        mid = 0
        while num != 0:
            mid += num % 10
            num //= 10
        return add_digits(mid)


def add_digits1(num):
    while num > 9:
        num = eval("+".join(n for n in str(num)))
    return num


if __name__ == "__main__":
    print(add_digits(38))
