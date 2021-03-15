# -*- coding: utf-8 -*-


import json
from json import JSONDecodeError

from marshmallow import fields, ValidationError, Schema


class JSONField(fields.Field):
    def _serialize(self, value, attr, obj):
        try:
            return json.dumps(value)
        except TypeError as err:
            raise ValidationError(str(err.args[0]))

    def _deserialize(self, value, attr, obj):
        try:
            return json.loads(value)
        except (TypeError, JSONDecodeError) as err:
            raise ValidationError(str(err.args[0]))


class PersonSchema(Schema):

    name = fields.String(required=True, allow_none=False)
    address = JSONField(required=False, allow_none=True)


if __name__ == "__main__":

    person_schema = PersonSchema(strict=True)

    data = {"name": "david", "address": ["123", "456"]}

    load_data = person_schema.load(data).data

    print(f"After load: {load_data}")

    data = {"name": "david", "address": {"country": "China"}}

    dump_data = person_schema.dump(data).data

    print(f"After dump: {dump_data}")
