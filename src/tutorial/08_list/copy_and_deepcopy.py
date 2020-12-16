# -*- coding: utf-8 -*-

from copy import copy, deepcopy


a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

# Use normal assignment operations to copy
d = c

print(id(c) == id(d))  # True - d is the same object as c
print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]


# Use a shallow copy
d = copy(c)

print(id(c) == id(d))  # False - d is now a new object
print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]


# Use a deep copy
d = deepcopy(c)

print(id(c) == id(d))  # False - d is now a new object
print(id(c[0]) == id(d[0]))  # False - d[0] is now a new object
