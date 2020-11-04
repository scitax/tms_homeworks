from random import randint
from typing import List

from numpy import array
import json

def generating_random_matrix_to(max_rows: int, max_columns: int, max_number: int):
    if not isinstance(max_rows, int) \
            or not isinstance(max_columns, int) \
            or not isinstance(max_number, int):
        print('int for max_columns, max_number, file_name or str for file_name is expexted')
        return None
    final_array = []
    for _ in range(max_rows):
        array_row = []
        for __ in range(max_columns):
            array_row.append(randint(0, max_number))
        final_array.append(array_row)
    return final_array

def set_matix_odd_elements_to_zerro(in_matrtix: list):
    new_matrix = []
    for row in in_matrtix:
        matrix_row = []
        for element in row:
            if not element % 2:
                element = 0
            matrix_row.append(element)
        new_matrix.append(matrix_row)
    return new_matrix

not_converted_matrix_for_json_name = 'matrix'
converted_matrix_for_json_name = 'converted matrix'

# writing matix to file
with open('matrix_contain.txt', 'w') as matrix_contain_file:
    matrix = generating_random_matrix_to(4,4,10)
    data = json.dumps({not_converted_matrix_for_json_name: matrix})
    matrix_contain_file.write(data)

# reading matitx form file
with open('matrix_contain.txt') as matrix_contain_file:
    matrix_contain_json_data = json.load(matrix_contain_file)

# reading converted matrix to file
with open('converted_matrix_contain.txt', 'w') as converted_matrix_file:
    matrix_to_convert = matrix_contain_json_data[not_converted_matrix_for_json_name]
    converted_matrix = set_matix_odd_elements_to_zerro(matrix_to_convert)
    data = json.dumps({converted_matrix_for_json_name: converted_matrix})
    converted_matrix_file.write(data)
