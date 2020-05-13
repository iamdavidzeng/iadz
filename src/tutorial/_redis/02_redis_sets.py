import time
import redis

REDIS_URI = "redis://localhost:6379/0"

client = redis.StrictRedis.from_url(REDIS_URI)

key = "delay:reindex:property-ids"

maximum_ids = 300


def add_sets(element):
    client.sadd("myset", element)


if __name__ == "__main__":
    counter = 1
    while True:
        print(f"hahah{counter}")
        try:
            time.sleep(1)
            add_sets(counter)
            counter += 1
        except Exception as e:
            print(e)
