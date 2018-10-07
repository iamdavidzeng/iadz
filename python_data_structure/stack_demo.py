#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack(object):

    def __init__(self, *args):
        self.__list = list(args)

    def __repr__(self):
        return repr(self.__list)

    def __len__(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop(-1)

    def get_count(self):
        return self.__list.__len__()

    def is_empty(self):
        if self.__list:
            return False
        return True


if __name__ == '__main__':
    demo = Stack(1, 2, 3, 4)
    print(demo)
    demo.push(5)
    print(demo)
    demo.pop()
    print(demo)
    print(demo.get_count())
    print(demo.is_empty())
