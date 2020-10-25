from math import pi
from functools import reduce

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Figure:
    def __init__(self):
        self.perimeter = None
        self.square = None

    def two_point_distance(self, point_1: Point, point_2: Point):
        distance = ((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)**0.5
        return distance


class Circle(Figure):
    def __init__(self, radius: float, center_point: Point):
        super(Circle, self).__init__()
        self.center_point = center_point
        self.radius = radius

    def figure_square(self):
        self.square = pi * self.radius ** 2

    def figure_perimeter(self):
        self.perimeter = 2 * pi * self.radius


class Triangle(Figure):
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        super(Triangle, self).__init__()
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def figure_square(self):
        self.square = 0.5 * abs(
            (self.point_1.x-self.point_3.x)*(self.point_2.y-self.point_3.y) -
            (self.point_2.x - self.point_3.x) * (self.point_1.y - self.point_3.y)
        )

    def figure_perimeter(self):
        self.perimeter = (
                self.two_point_distance(self.point_1, self.point_2) +
                self.two_point_distance(self.point_1, self.point_3) +
                self.two_point_distance(self.point_2, self.point_3)
        )


class Square(Figure):
    def __init__(self, point_1: Point, point_2: Point):
        super(Square, self).__init__()
        self.point_1 = point_1
        self.point_2 = point_2

    def figure_square(self):
        self.square = abs((self.point_1.x - self.point_1.x)*(self.point_1.y-self.point_2.y))

    def figure_perimeter(self):
        self.perimeter = 2 * (abs(self.point_1.x - self.point_1.x)+ abs(self.point_1.y-self.point_2.y))





float


