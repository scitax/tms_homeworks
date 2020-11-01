from matrix_utils import Matrix
from matrix_utils import reduce


def find_min_element(matrix_arg: Matrix):
    min_element = matrix_arg.data[0][0]
    for current_row in range(matrix_arg.m):
        min_element = reduce(lambda x, y: y if y < x else x, matrix_arg.data[current_row], min_element)
    return min_element


def find_max_element(matrix_arg: Matrix):
    max_element = matrix_arg.data[0][0]
    for current_row in range(matrix_arg.m):
        max_element = reduce(lambda x, y: y if y > x else x, matrix_arg.data[current_row], max_element)
    return max_element


def find_sum_of_elements(matrix_arg: Matrix):
    sum_of_elements = matrix_arg.data[0][0]
    for current_row in range(matrix_arg.m):
        sum_of_elements = reduce(lambda x, y: x + y, matrix_arg.data[current_row], sum_of_elements)
    return sum_of_elements
