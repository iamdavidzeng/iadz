# -*- coding: utf-8 -*-


def replay():
    while True:
        request()


def request():
    for i in range(10):
        if i == 8:
            break
        print(f"i: {i}")


if __name__ == "__main__":

    replay()
