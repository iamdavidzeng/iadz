#!/usr/bin/env python
# -*- coding: utf-8 -*-


def first_exc():
    try:
        second_exc()
    except Exception as e:
        print("fail：%s" % e)


def second_exc():
    demo = "0"
    demo += 1


if __name__ == "__main__":
    first_exc()
