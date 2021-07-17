"""
Single Responsibility Principle
"""


from typing import Any

# Break the SRP
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def save(self, animal: Any):
        pass


# Satisfy the SRP
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal) -> Animal:
        pass
