"""
Liskov Substitution Principle
"""


from typing import List


class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


animals = [Lion()]


def animal_leg_count(animals: List[Animal]):
    for animal in animals:
        print(animal.leg_count())


animal_leg_count(animals)