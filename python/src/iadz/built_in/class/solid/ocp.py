"""
Open-Closed Principle
"""
from typing import List

# Break the OCP
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


animals = [Animal("lion"), Animal("mouse")]


def animal_sound(animals: List[Animal]):
    for animal in animals:
        if animal.name == "lion":
            print("roar")
        elif animal.name == "mouse":
            print("squeak")


animal_sound(animals=animals)


animals = [Animal("lion"), Animal("mouse"), Animal("snake")]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == "lion":
            print("roar")
        elif animal.name == "mouse":
            print("squeak")
        elif animal.name == "snake":
            print("hiss")


animal_sound(animals)


# OCP
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self) -> str:
        pass


class Lion(Animal):
    def make_sound(self) -> str:
        return "roar"


class Mouse(Animal):
    def make_sound(self) -> str:
        return "squeak"


class Snake(Animal):
    def make_sound(self) -> str:
        return "hiss"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animal_sound()
