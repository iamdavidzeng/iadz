#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contextlib import contextmanager


LANGUAGE_CONTEXT_KEY = "language"


@contextmanager
def language_override(worker_ctx, language):

    original_language = worker_ctx.data.get(LANGUAGE_CONTEXT_KEY)
    worker_ctx.data[LANGUAGE_CONTEXT_KEY] = language
    yield
    worker_ctx.data[LANGUAGE_CONTEXT_KEY] = original_language


class Worker(object):

    data = {"name": "david.zeng", "gender": "male", "language": "zh-cn"}


if __name__ == "__main__":
    worker = Worker()

    with language_override(worker, "en-us"):
        print(worker.data)

    print(worker.data)
