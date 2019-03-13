#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@name: common_str.py
@author: Aeiou
@time: 18-10-25 下午8:31

get the most common str of element in list
"""


def get_common_str(l1):
    guard = l1[0]
    ret = ""
    for index, value in enumerate(guard):
        for j in l1[1:]:
            if len(j) > index and value != j[index]:
                return ret
        ret += value


if __name__ == '__main__':
    l1 = ["abc", "ac", "d"]
    rsp = get_common_str(l1)
    print(rsp)
