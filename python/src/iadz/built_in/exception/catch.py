# -*- coding: utf-8 -*-


class NotFound(Exception):
    pass


if __name__ == "__main__":

    try:
        raise NotFound()
    except NotFound:
        print("catch it!!")
