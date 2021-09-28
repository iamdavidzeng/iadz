import time
import random
import threading


class Task(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

    def task_1(self):
        while True:
            print("starting task1")
            time.sleep(random.randint(1, 5))
            print("task1 completed!")

    def task_2(self):
        while True:
            print("starting task2")
            time.sleep(random.randint(1, 5))
            print("task2 completed!")

    def run(self):
        thread1 = threading.Thread(target=self.task_1)
        thread2 = threading.Thread(target=self.task_2)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()


if __name__ == "__main__":
    task = Task()
    task.run()
