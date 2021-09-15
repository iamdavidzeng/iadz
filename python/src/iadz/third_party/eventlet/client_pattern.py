import time
from typing import Tuple

import eventlet
from eventlet.green.urllib import request

urls = [
    "https://www.google.com/intl/en_ALL/images/logo.gif",
    "http://python.org/images/python-logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url: str) -> Tuple:
    print(f"starting {url}")
    body = request.urlopen(url).read()
    return url, body


if __name__ == "__main__":

    start = time.time()
    pool = eventlet.GreenPool(200)
    for url, body in pool.imap(fetch, urls):
        print("got body from", url, "of length", len(body))
    count = time.time() - start
    print(count)

    start = time.time()
    from urllib.request import urlopen

    for url in urls:
        urlopen(url).read()
    count = time.time() - start
    print(count)
