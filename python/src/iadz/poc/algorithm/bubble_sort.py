#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble(item_list):
    length = len(item_list) - 1
    for i in range(length):
        for num in range(length - i):
            if item_list[num] > item_list[num + 1]:
                mid = item_list[num + 1]
                item_list[num + 1] = item_list[num]
                item_list[num] = mid


if __name__ == "__main__":
    demo = [123, 5235, 34, 23, 5, 3]
    bubble(demo)
    print(demo)
