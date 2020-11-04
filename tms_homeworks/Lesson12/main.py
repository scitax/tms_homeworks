from geometry import Triangle, Circle, Point, Square

if __name__ == '__main__':
    figure_list = [
        Triangle(Point(0, 0), Point(0, 2), Point(3, 4)),
        Circle(2, Point(0, 0)),
        Square(Point(0, 0), Point(2, 2))
    ]

    for figure in figure_list:
        figure.figure_square()
        figure.figure_perimeter()
        print(f'{figure.square},{figure.perimeter}')
