import time
from typing import Tuple

import eventlet
from eventlet.green.urllib import request


pool = eventlet.GreenPool(200)
pile = eventlet.GreenPile(pool)
urls = [
    "https://www.google.com/intl/en_ALL/images/logo.gif",
    "http://python.org/images/python-logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url: str) -> Tuple:
    print(f"starting {url}")
    body = request.urlopen(url).read()
    return url, body


def start_(urls: str, count=0):
    print(urls)

    with eventlet.Timeout(10):
        for url, body in pool.imap(fetch, urls):
            count += 1
            print("got body from", url, "of length", len(body))
            yield count


if __name__ == "__main__":

    start = time.time()
    pile.spawn(start_, urls)
    for i in pile:
        print([e for e in i])
    # start_(urls)
    count = time.time() - start
    print(count)
