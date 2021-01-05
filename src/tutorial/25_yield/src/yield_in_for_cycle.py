#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def yield_in_cycle(lst):
    for i in lst:
        yield i


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]
    generator = yield_in_cycle(num_list)
    try:
        for count in range(10):
            print(next(generator))
    except StopIteration as exc:
        raise exc
