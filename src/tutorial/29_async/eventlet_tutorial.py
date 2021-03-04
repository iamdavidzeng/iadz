# -*- coding: utf-8 -*-

import eventlet
from eventlet.green.urllib.request import urlopen

urls = [
    "http://www.google.com/intl/en_ALL/images/logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url):
    return urlopen(url).read()


pool = eventlet.GreenPool()

for body in pool.imap(fetch, urls):
    print("got body", len(body))
