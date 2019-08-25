# -*- coding: utf-8 -*-


# def is_happy(num):

#     try:
#         while num != 1:
#             num = eval("+".join(str(int(n) ** 2) for n in str(num)))
#         return True
#     except:
#         return False


def is_happy(n):
    old = {1}
    while n not in old:
        old.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1


if __name__ == "__main__":
    print(is_happy(19))
