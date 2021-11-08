"""
Only the await-able object can be used by `await`.
"""

# coroutine
import asyncio


async def nested():
    return 42


async def main_1():
    print("main 1")

    # Only return a coroutine object.
    nested()

    # Execute the coroutine object.
    print(await nested())


asyncio.run(main_1())


# Task
async def main_2():
    print("main 2")

    task = asyncio.create_task(nested())

    result = await task
    print(result)


asyncio.run(main_2())


# Future object
async def main_3():
    print("main 3")

    loop = asyncio.get_running_loop()
    future = loop.create_future()

    return future


asyncio.run(main_3())

# gather
async def foo(name: str, number: int):
    print(f"Name: {name}")

    await asyncio.sleep(number)

    return name[::-1]


async def main():

    result_1, result_2 = await asyncio.gather(
        foo("Foo", 2),
        foo("Bar", 4),
    )

    print(result_1, result_2)


asyncio.run(main())
