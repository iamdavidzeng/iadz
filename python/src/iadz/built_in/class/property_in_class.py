# -*- coding: utf-8 -*-


class Person:
    def __init__(self, first_name, last_name) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    @property
    def username(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":

    david = Person("david", "zeng")

    print(david.username)
