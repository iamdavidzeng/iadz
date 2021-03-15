# -*- coding: utf-8 -*-


from functools import wraps


class CustomizeException(Exception):

    pass


def catch_and_dispatch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print("i am here...")
            raise exc

    return wrapper


@catch_and_dispatch
def raise_an_error():
    raise CustomizeException()


if __name__ == "__main__":
    raise_an_error()
