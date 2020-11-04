from matrix_utils import randint


class Matrix(object):
    data = None
    n = None
    m = None

    def __init__(self, n: int = 5, m: int = 5, a: int = 0, b: int = 0):
        """
        matrix with random elements
        :param n: number of columns
        :param m: number of rows
        :param a: randint min element
        :param b: randint max element
        """
        Matrix.n = n
        Matrix.m = m
        self.a = a
        self.b = b
        self.create_matrix()

    def __str__(self):
        matrix_print = ''
        for current_row in range(Matrix.m):
            for current_element in range(Matrix.n):
                matrix_print = f'{matrix_print} {Matrix.data[current_row][current_element]}'
            matrix_print = matrix_print + '\n'
        return matrix_print


    def __copy__(self):

    def create_matrix(self):
        Matrix.data = [[randint(self.a, self.b) for _ in range(Matrix.n)] for _ in range(Matrix.m)]
