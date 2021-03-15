#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps

from marshmallow import Schema, fields, ValidationError, post_dump


class Student(Schema):

    id = fields.Int(allow_none=False)
    name = fields.Str(allow_none=False)
    grade = fields.Int(allow_none=False)
    alternate_text = fields.Str(allow_none=True, default=None)
    password = fields.Str(allow_none=True, load_only=True)

    @post_dump()
    def set_alt_text(self, data):
        data["alt_text"] = data.get("alternate_text")


def validate_input(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):

            print("call_args: ['args': %s, 'kwargs': %s]" % (args, kwargs))
            args_list = list(args)
            args_list[0] = _validate_data(schema, args[0])

            return func(self, *args_list, **kwargs)

        return wrapper

    return decorator


def _validate_data(schema, data):
    try:
        data_ = schema(strict=True).dump(data).data
        print("data_after_load: %s" % data_)
        return data_
    except ValidationError as exc:
        raise ValueError(*exc.args)


class DataAfterSchemaLoad(object):
    def __init__(self, data):
        self.student = self.create_student(data)

    @validate_input(Student)
    def create_student(self, data):
        return data


if __name__ == "__main__":
    mock_student = {
        "id": 1,
        "name": "david",
        "grade": "88",
        "alternate_text": "hello, world!",
        # "password": "mock_password",
    }
    student = DataAfterSchemaLoad(data=mock_student)

    student_1 = student.create_student(mock_student)

    print("data_after_load: %s" % student_1)
