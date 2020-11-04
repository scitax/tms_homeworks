from abc import ABC, abstractmethod


class Feline(ABC):
    __feline_quantity = 0

    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight
        Feline.__feline_quantity += 1

    @abstractmethod
    def say_hi(self):
        raise NotImplemented

    @abstractmethod
    def viskas(self):
        raise NotImplemented

    @property
    def feline_quantity(self):
        return Feline.__feline_quantity


class Feline(ABC):
    __feline_quantity = 0

    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight
        Feline.__feline_quantity += 1

    @abstractmethod
    def say_hi(self):
        raise NotImplemented

    @abstractmethod
    def viskas(self):
        raise NotImplemented

    @property
    def feline_quantity(self):
        return Feline.__feline_quantity
