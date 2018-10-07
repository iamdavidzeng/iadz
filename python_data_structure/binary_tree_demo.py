#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.data)


class BinarySearchTree(object):

    def __init__(self):
        self.size = 0
        self.root = None

    def is_empty(self):
        return self.size == 0

    def _dict(self, item):
        if item:
            mid = dict()
            mid['root'] = item
            mid['left'] = item.left
            mid['right'] = item.right
            print(mid)
        if item.left:
            self._dict(item.left)
        if item.right:
            self._dict(item.right)
        return all

    def __repr__(self):
        self._dict(self.root)
        return repr('success')

    def _left(self, node, item):
        if node.left is None:
            return node
        else:
            if item.data < node.data:
                return self._left(node.left, item)
            elif item.data > node.data:
                return self._right(node.right, item)

    def _right(self, node, item):
        if node.right is None:
            return node
        else:
            if item.data < node.data:
                return self._left(node.left, item)
            elif item.data > node.data:
                return self._right(node.right, item)

    def _correct_location(self, node, item):
        if item.data < node.data:
            return self._left(node, item)
        elif item.data > node.data:
            return self._right(node, item)

    def append(self, item):
        if isinstance(item, Node):
            pass
        else:
            item = Node(item)
        if not self.root:
            self.root = item
            self.size += 1
        else:
            correct_node = self._correct_location(self.root, item)
            if item.data < correct_node.data:
                correct_node.left = item
                self.size += 1
            elif item.data > correct_node.data:
                correct_node.right = item
                self.size += 1
            else:
                pass

    def get_length(self):
        return self.size

    def pre_travel(self):
        self._pre(self.root)

    def _pre(self, node):
        if node:
            print(node)
            self._pre(node.left)
            self._pre(node.right)

    def mid_travel(self):
        self._mid(self.root)

    def _mid(self, node):
        if node:
            self._mid(node.left)
            print(node)
            self._mid(node.right)

    def back_travel(self):
        self._back(self.root)

    def _back(self, node):
        if node:
            self._back(node.left)
            self._back(node.right)
            print(node)

# ################other way#####################

    def add_node(self, item):
        if isinstance(item, Node):
            pass
        else:
            item = Node(item)
        if not self.root:
            self.root = item
            self.size += 1
        else:
            self._add_child(self.root, item)
            self.size += 1

    def _add_child(self, node, item):
        if not node:
            return item
        if node.data > item.data:
            node.left = self._add_child(node.left, item)
        if node.data < item.data:
            node.right = self._add_child(node.right, item)


if __name__ == '__main__':
    search_tree = BinarySearchTree()
    for i in range(10):
        search_tree.append(i)
    print(search_tree)
    search_tree.back_travel()
