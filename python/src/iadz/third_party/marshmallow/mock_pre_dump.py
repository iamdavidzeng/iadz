from marshmallow import Schema, fields
from marshmallow.decorators import post_dump


class Listing(Schema):

    minimum_price = fields.Decimal()
    discounted_price = fields.Decimal()

    @post_dump
    def get(self, data):

        print("=======listing======")

        data["discounted_price"] = 100

        return data


class Unit(Schema):

    listings = fields.Nested(Listing, many=True)

    @post_dump
    def get(self, data):

        print("=========unit======")

        return data


class Property(Schema):

    units = fields.Nested(Unit, many=True)

    @post_dump
    def get1(self, data):

        print("=========property2======")

        return data

    @post_dump
    def get(self, data):

        print("=========property1======")

        return data


if __name__ == "__main__":
    data = {"units": [{"listings": [{"minimum_price": 100}]}]}
    print(Property(strict=True).dump(data).data)
