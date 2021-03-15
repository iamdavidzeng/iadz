# -*- coding: utf-8 -*-


lst_1 = [(4455.0, 'NULL'), (4455.0, 'NULL')]

lst_2 = [(4455.0, 'NULL', 'NULL'), (4455.0, 'NULL', 'NULL')]


lst_3 = ["david.zeng1", "david.zeng2"]


values_1 = ",".join((str(i) for i in lst_1))
print(f"values_1: {values_1}")

values_2 = ",".join((str(i) for i in lst_2))
print(f"values_2: {values_2}")

values_3 = "".join(map(lambda x: f"<@{x}>", lst_3))
print(f"values_3: {values_3}")
