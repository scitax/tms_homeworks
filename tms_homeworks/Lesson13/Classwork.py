from random import randint, choice
from string import ascii_uppercase
from abc import ABC, abstractmethod


class Car:
    last_model = None
    counter = 0

    def __init__(self, model: str):
        self._model = model
        Car.last_model = model
        Car.counter += 1

    def __str__(self):
        return self._model

    @classmethod
    def get_counter(cls):
        return cls.counter


class Pet(ABC):
    @staticmethod
    def get_random_name():
        return f'{choice(ascii_uppercase)}-{randint(0, 100)}'

    @abstractmethod
    def voice(self):
        print('Hello!')


class Horse(Pet):
    def voice(self):
        print('I-go-go!')


class Donkey(Pet):
    def voice(self):
        print('Yeee-haaa!')


class Mule(Donkey, Horce):
    pass


class Page_number_error(Exception):
    pass


class Book:
    def __init__(self, page_number, year, author, price):
        if not page_number == int:
            raise Page_number_error
        self.page_number = page_number
        self.year = year
        self.author = author
        self.price = price


if __name__ == '__main__':
    honda = Car('Honda')
    toyouta = Car('Toyouta')
    mazda = Car('Mazda')

    print(Car.get_counter())

    rand_pet = Pet()
    print(Pet.get_random_name())

    a = Mule()
    print(a.voice())
