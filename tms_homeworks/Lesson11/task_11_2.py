class Car:
    def __init__(self, make: str, model: str, year: int, speed: int = 0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_upp(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def turn_over(self):
        self.__speed = -self.__speed

    @property
    def speed(self):
        return self.__speed

