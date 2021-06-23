# -*- coding: utf-8 -*-

subjects = ["math", "chemistry", "biology", "pyhsics"]
grades = [100, 83, 90, 92]


grades_dict = dict(zip(subjects, grades))
print(grades_dict)



columns = ["first_name", "last_name"]
resource = ["David", "Zeng"]
users = dict(zip(columns, resource))
print(users)
