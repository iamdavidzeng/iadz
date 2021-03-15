# -*- coding: utf-8 -*-

from functools import wraps
from queue import Queue


def dispatch_from_queue(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        result = func(self, *args, **kwargs)

        while not self.queue.empty():
            event_name, payload = self.queue.get()
            print(event_name, payload)

        return result

    return wrapper


class DummyService:

    queue = Queue()

    @dispatch_from_queue
    def create_user(self, first_name, last_name):
        user = {"first_name": first_name, "last_name": last_name}
        event = ("user_created", user)
        self.queue.put(event)
        return user


if __name__ == "__main__":

    dummy_service = DummyService()

    dummy_service.create_user("david", "zeng")
