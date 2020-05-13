# -*- coding: utf-8 -*-
from enum import Enum

from marshmallow import fields, Schema


class PersonType(Enum):

    kind = "Kind"
    bad = "Bad"
    gentle = "Gentle"
    confused = "Confused"


class EnumField(fields.Field):


    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        return super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        if value not in self.enum:
            raise ValidationError(
                "{} is not not a member of {}".format(value, self.enum)
            )
        return value.value

    def _deserialize(self, value, attr, data):
        try:
            return self.enum(value)
        except ValueError as exc:
            raise ValidationError(exc.args[0])



class PersonCreateSchema(Schema):

    person_type = EnumField(PersonType, required=True, allow_none=False)


if __name__ == "__main__":
    before_load = {"person_type": "Kind"}
    after_load = PersonCreateSchema(strict=True).load(before_load).data
    print(after_load)
