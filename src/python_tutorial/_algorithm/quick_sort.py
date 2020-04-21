#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@name: quick_sort.py
@author: Aeiou
@time: 18-10-7 上午10:40
"""


def quick_sort(items, start, end):
    if start < end:
        low, high = start, end
        base = items[low]
        while low < high:
            while low < high and items[high] >= base:
                high -= 1
            items[low] = items[high]
            while low < high and items[low] <= base:
                low += 1
            items[high] = items[low]
        items[low] = base

        quick_sort(items, start, low - 1)
        quick_sort(items, high + 1, end)
    return items


if __name__ == '__main__':
    demo = [49, 38, 27, 64, 96, 32]
    new = quick_sort(demo, 0, len(demo) - 1)
    print(new)
