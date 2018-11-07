#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@name: coroutine_demo.py
@author: Aeiou
@time: 18-11-7 下午1:11
"""

import asyncio


def consume():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consuming %s...' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('producing %s...' % n)
        r = c.send(n)
        print('consumer return: %s' % r)
    c.close()


@asyncio.coroutine
def hello():
    print('Hello, world!')
    r = yield from asyncio.sleep(5)
    print('Hello again!')


async def halo():
    print('Hello, world!')
    r = await asyncio.sleep(5)
    print('Hello again!')


@asyncio.coroutine
def demo():
    print('test')
    r = yield from asyncio.sleep(2)
    print('test demo')


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(hello())
    loop.close()
