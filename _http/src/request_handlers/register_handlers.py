# -*- coding: utf-8 -*-

import functools


def get(path):
    def _get(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__method__ = "GET"
        wrapper.__route__ = path
        return wrapper
    return _get


class App(object):

    def register(self, method, path, handler):
        if self.__class__:
            pass
        print(f"method: {method}\n"
              f"path: {path}\n"
              f"handler: {handler}"
              )


app = App()


def add_routes(module_name):
    dot = module_name.rfind(".")
    if dot == -1:
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[dot+1:]
        mod = __import__(name, globals(), locals())

    for item in dir(mod):

        if item.startswith("_"):
            continue

        func = getattr(mod, item)
        if callable(func):
            path = getattr(func, "__route__", None)
            method = getattr(func, "__method__", None)
            if path and method:
                add_route(method, path, func)


def add_route(method, path, func):
    app.register(method, path, RequestHandlers(func))


class RequestHandlers(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        kwargs = request.match_info.items()

        response = self.func(**kwargs)

        return response


if __name__ == "__main__":
    add_routes("handlers")
