#!/usr/bin/env python3
# -*- coding: utf-8 -*-


SIGNUP_TYPES = {
    "phone": "111",
    "email": "a@b.com",
    "facebook_id": "1234",
}


class ValidationError(Exception):
    pass


def return_signup_value(data):
    for type_ in SIGNUP_TYPES:
        if data.get(type_):
            print("counting...")
            # once type_ in SIGNUP_TYPES have value in data, don't raise Error
            return

    raise ValidationError("phone, email or facebook_id has to be presented.")


if __name__ == "__main__":
    return_signup_value({"phone": "1234", "facebook_id": "1234"})
