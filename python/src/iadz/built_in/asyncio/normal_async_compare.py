import time
import asyncio


class Normal:
    def sleep(self):
        time.sleep(1)

    def sum(self, name, numbers):
        total = 0
        for number in numbers:
            self.sleep()
            total += number
        print(f"Task {name}: Sum = {total}\n")

    def main(self):
        start = time.time()
        tasks = [self.sum("A", [1, 2]), self.sum("B", [1, 2, 3])]
        end = time.time()
        print(f"Time: {end-start:.2f} sec")


class WrongAsync:
    async def sleep(self):
        time.sleep(1)

    async def sum(self, name, numbers):
        total = 0
        for number in numbers:
            await self.sleep()
            total += number
        print(f"Task {name}: Sum = {total}\n")

    def main(self):
        loop = asyncio.get_event_loop()
        start = time.time()
        tasks = [
            loop.create_task(self.sum("A", [1, 2])),
            loop.create_task(self.sum("B", [1, 2, 3])),
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        end = time.time()
        print(f"Time: {end-start:.2f} sec\n")

        # loop.close()


class RightAsync:
    async def sleep(self):
        await asyncio.sleep(1)

    async def sum(self, name, numbers):
        total = 0
        for number in numbers:
            await self.sleep()
            total += number
        print(f"Task {name}: Sum = {total}\n")

    def main(self):
        loop = asyncio.get_event_loop()
        start = time.time()
        tasks = [
            loop.create_task(self.sum("A", [1, 2])),
            loop.create_task(self.sum("B", [1, 2, 3])),
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        end = time.time()
        print(f"Time: {end-start:.2f} sec\n")

        loop.close()


if __name__ == "__main__":
    for cls_ in [WrongAsync, RightAsync]:
        cls_().main()
