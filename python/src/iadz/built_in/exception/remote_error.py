# -*- coding: utf-8 -*-

import inspect

errors = {}


def remote_error(exc_path):
    def wrapper(exc_type):
        errors[exc_path] = exc_type
        return exc_type

    return wrapper


@remote_error("__main__.NewUserNotFound")
class UserNotFound(Exception):
    pass


@remote_error("__main__.UserNotFound")
class NewUserNotFound(Exception):
    pass


def get_module_path(exc_type):
    module = inspect.getmodule(exc_type)
    return f"{module.__name__}.{exc_type.__name__}"


def serialize(exc):
    return {
        "exc_path": get_module_path(type(exc)),
        "exc_type": type(exc).__name__,
    }


def deserialize(exc):
    key = exc.get("exc_path")
    if key in errors:
        return errors[key]()

    return Exception()


def get_user():
    return {"result": None, "error": serialize(UserNotFound())}


def get_new_user():
    response = get_user()
    if response.get("error"):
        raise deserialize(response["error"])


def catch_expected_error():
    try:
        get_new_user()
    except NewUserNotFound as exc:
        print(f"Catch exception: {type(exc)}")


if __name__ == "__main__":

    catch_expected_error()
