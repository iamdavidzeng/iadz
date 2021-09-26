#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


def select_sort(item_list):
    length = len(item_list)
    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if item_list[index] > item_list[j]:
                index = j
        item_list[i], item_list[index] = item_list[index], item_list[i]


@pytest.mark.parametrize(
    ["args", "expected"], [([123, 23, 1, 23, 543, 64], [1, 23, 23, 64, 123, 543])]
)
def test_select_sort(args, expected):
    select_sort(args)
    assert args == expected
