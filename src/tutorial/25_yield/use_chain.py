# -*- coding: utf-8 -*-

from itertools import chain

iterator = chain("ABC", "DEF")

print([i for i in iterator])
