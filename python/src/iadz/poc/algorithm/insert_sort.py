#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insert_sort(item_list):
    length = len(item_list)
    for i in range(1, length):
        mid = item_list[i]
        for j in range(i, -1, -1):
            if mid < item_list[j - 1]:
                item_list[j] = item_list[j - 1]
            else:
                break
        item_list[j] = mid


if __name__ == "__main__":
    demo = [23, 12, 543, 765, 45]
    insert_sort(demo)
    print(demo)
