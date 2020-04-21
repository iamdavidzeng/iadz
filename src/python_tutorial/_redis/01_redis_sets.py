# -*- coding: utf-8 -*-

import redis

REDIS_URI = "redis://localhost:6379/0"

client = redis.StrictRedis.from_url(REDIS_URI)

key = "myset"

maximum_ids = 300


def add_sets():
    lst = (1, 2, 3, 4, 5)
    client.sadd("myset", *lst)


def get_sets():
    # b = f"""
    # local values=redis.call('SMEMBERS', '{key}');
    # redis.call('DEL', '{key}');
    # return values"""
    # sets = client.eval(b, 0)
    # print(sets)
    sets = client.spop(key, 100)
    print(list(map(lambda x: int(x.decode()), sets)))
    if client.smembers(key):
        # dispatch event
        pass


if __name__ == "__main__":
    add_sets()
    get_sets()
