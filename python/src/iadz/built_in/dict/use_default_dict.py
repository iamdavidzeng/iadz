# -*-  coding: utf-8 -*-

from collections import defaultdict

event_handlers = defaultdict(dict)

DEFUALT_VERSION = "v1"


def register_event_handler(event_name, version=None):
    version = version or DEFUALT_VERSION

    def register(func):
        event_handlers[version][event_name] = func
        return func

    return register


handle_event = register_event_handler

CURRENT_VERSION = "v2"


class RegisterEvents(object):
    @handle_event("source.failed", version=CURRENT_VERSION)
    def handle_source_failed(self, event_name):
        return "handle_source_failed"

    @handle_event("source.succeed", version=CURRENT_VERSION)
    def handle_source_succeed(self, event_name):
        return "handle_source_succeed"


if __name__ == "__main__":
    print(event_handlers)
