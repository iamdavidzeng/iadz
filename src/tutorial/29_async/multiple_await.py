# -*- coding: utf-8 -*-

import asyncio
import time


async def hello(delay: int):
    await asyncio.sleep(delay)
    print(f"hello")


async def world(delay: int):
    await asyncio.sleep(delay)
    print(f"world")


async def another_say_hi():
    print("hi, world!")


async def greet():
    print(f"Started at {time.strftime('%X')}")

    await hello(1)

    await world(2)

    print(f"Finished at {time.strftime('%X')}")


async def greet_again():

    await another_say_hi()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([greet(), greet_again()]))
