# -*- coding: utf-8 -*-

import sys, os

project_root = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, project_root)

from a.constants import Person

print(Person.first_name)
