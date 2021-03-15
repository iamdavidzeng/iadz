#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_sort(item_list):
    length = len(item_list)
    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if item_list[index] > item_list[j]:
                index = j
        item_list[i], item_list[index] = item_list[index], item_list[i]


if __name__ == "__main__":
    demo = [123, 23, 1, 23, 543, 64]
    select_sort(demo)
    print(demo)
