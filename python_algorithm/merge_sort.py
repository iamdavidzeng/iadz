#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(item_list):
    if len(item_list) == 1:
        return item_list
    mid = len(item_list) // 2
    previous = merge_sort(item_list[:mid])
    _next = merge_sort(item_list[mid:])
    return merge(previous, _next)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


if __name__ == '__main__':
    demo = [23, 523, 51, 216, 87]
    new = merge_sort(demo)
    print(new)
