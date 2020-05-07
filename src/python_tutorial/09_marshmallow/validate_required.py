# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class User(Schema):

    name = fields.String(required=True, allow_none=False)
    gender = fields.String(required=True, allow_none=False)
    created_at = fields.DateTime(required=False, allow_none=True)


if __name__ == "__main__":
    user = {"name": "iamdavidzeng", "gender": "male"}
    load_user = User(strict=True).load(user).data
    print(load_user)
