#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        return repr(self.data)


class LinkList(object):
    def __init__(self):
        self.size = 0
        self.header = None

    def __repr__(self):
        link_list = []
        item = self.header
        while item.next:
            link_list.append(item.data)
            item = self._next(item, 1)
        return repr(link_list)

    def _last(self, item):
        # if item.next is None:
        #     return item
        # else:
        #     return self._last(item.next)
        return item if item.next is None else self._last(item.next)

    def append(self, item):
        if isinstance(item, Node):
            pass
        else:
            item = Node(item)
        if not self.header:
            self.header = item
            self.size += 1
        else:
            last = self._last(self.header)
            last.next = item
            self.size += 1

    @staticmethod
    def _next(item, count):
        if not isinstance(item, Node):
            raise Exception("need a Node")
        while count:
            count -= 1
            item = item.next
        return item

    def update(self, index, item):
        if isinstance(item, Node):
            pass
        else:
            item = Node(item)
        update_item = self._next(self.header, index)
        update_item.data = item

    def insert(self, index, item):
        if isinstance(item, Node):
            pass
        else:
            item = Node(item)
        insert_item = self._next(self.header, index)
        item.next = insert_item.next
        insert_item.next = item
        self.size += 1

    def getitem(self, index):
        item = self._next(self.header, index)
        return item.data

    def delete(self, index):
        if index == 0:
            self.header = self.header.next
            self.size -= 1
        else:
            item = self._next(self.header, index - 1)
            item.next = item.next.next
            self.size -= 1

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    link_list = LinkList()
    for i in range(5):
        link_list.append(i)
    print(link_list)
    print(link_list.getitem(2))
    link_list.insert(2, 10)
    print(link_list)
    link_list.delete(1)
    print(link_list)
