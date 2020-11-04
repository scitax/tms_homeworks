from matrix_utils import Matrix, matrix_funcs

if __name__ == '__main__':
    a = Matrix(3, 3, 0, 10)

    print(a)
    print(matrix_funcs.find_max_element(a))
    print(matrix_funcs.find_min_element(a))
    print(matrix_funcs.find_sum_of_elements(a))