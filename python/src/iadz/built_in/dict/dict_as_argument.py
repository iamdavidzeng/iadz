# -*- coding: utf-8 -*-
from stripe.stripe_object import StripeObject
from stripe.util import convert_to_stripe_object


metadata = convert_to_stripe_object({"user_id": 1})

print(metadata)


def update_dict(name, gender, metadata):

    metadata.update(user_id=1)

    print(metadata)


if __name__ == "__main__":

    metadata = {"nick": "iamdavidzeng"}

    update_dict(1, 2, metadata=metadata)

    print(metadata)
