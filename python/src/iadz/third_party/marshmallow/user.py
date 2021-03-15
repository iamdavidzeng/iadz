#!/user/bin/env python3
# -*- coding: utf-8 -*-


from functools import wraps

from marshmallow import Schema, fields, post_dump, post_load


class User(Schema):

    name = fields.Str(required=False, allow_none=True, dump_to="origin_name")
    address = fields.Str(required=False, allow_none=True)
    password = fields.Str(required=False, allow_none=True)
    # read-only
    first_name = fields.Str(dump_only=True)
    # write-only
    last_name = fields.Str(load_only=True)

    # @post_load()
    # def add_gender_to_data(self, data):
    #     data['gender'] = data.get('gender') or None


def validate_input(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("data: %s" % args)
            args_list = list(args)
            args_list[0] = schema(strict=True).load(args[0]).data
            return func(*args_list, **kwargs)

        return wrapper

    return decorator


@validate_input(User)
def validate_user(data):
    print("data_after_load: %s" % data)
    return data


if __name__ == "__main__":
    mock_student = {
        "name": "mock_name",
        "address": "mock_address",
        "password": "mock_password",
        "first_name": "David",
        "last_name": "Zeng",
    }
    data_after_load = validate_user(mock_student)

    data_after_dump = User(strict=True).dump(mock_student).data

    print(
        "data_after_dump: %s" % data_after_dump,
        "dump_to: %s" % data_after_dump.get("name"),
    )
