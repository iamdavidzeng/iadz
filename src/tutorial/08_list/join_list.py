# -*- coding: utf-8 -*-


lst_1 = [(4455.0, 'NULL'), (4455.0, 'NULL')]

lst_2 = [(4455.0, 'NULL', 'NULL'), (4455.0, 'NULL', 'NULL')]


values_1 = ",".join((str(i) for i in lst_1))
print(f"values_1: {values_1}")

values_2 = ",".join((str(i) for i in lst_2))
print(f"values_2: {values_2}")
