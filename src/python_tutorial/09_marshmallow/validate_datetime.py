# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class TimeLine(Schema):
    invoce_datetime = fields.DateTime()
    due_datetime = fields.DateTime()


if __name__ == "__main__":

    specific_moment = {
        "invoce_datetime": "2020-5-12 10:00:00",
        "due_datetime": "2020-5-12 10:00:00",
    }

    load_sm = TimeLine(strict=True).load(specific_moment).data

    print(load_sm)
