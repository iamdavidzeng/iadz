#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
统计一个数从0开始到自己，其中包含1的数字的个数，例如g1(13) = 5[1, 10, 11, 12, 13],
只能使用数学方式实现.
"""

def count_num(num):
    a, b = divmod(num, 10)
    if a == 1 or b == 1:
        return True
    if a > 10:
        return count_num(a)
    return False


def g1(num):
    sum = 0
    for i in range(num+1):
        if count_num(i):
            sum += 1
    return sum


if __name__ == '__main__':
    demo_num = 122
    print(g1(demo_num)) 
