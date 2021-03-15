#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue(object):
    def __init__(self, *args):
        self.queue = [*args]
        self.max_length = 5

    def __repr__(self):
        return repr(self.queue)

    def push(self, *item):
        for i in item:
            if len(self.queue) < self.max_length:
                self.queue.append(i)
            else:
                self.queue.pop(0)
                self.queue.append(i)

    def pop(self):
        return self.queue.pop(0)

    def get_header(self):
        return self.queue[0]

    def get_length(self):
        return len(self.queue)

    def is_empty(self):
        if self.queue:
            return True
        return False


if __name__ == "__main__":
    queue = Queue()
    print(queue)
    for i in range(10):
        queue.push(i)
    print(queue)
    queue.pop()
    print(queue)
    print(queue.get_header())
    print(queue.get_length())
    print(queue.is_empty())
