# task 1

# task 1.1

list_parameters = [1.4, 5.5]
tuple_parameteres = (1.4, 5.5)
set_parameters = {1.4, 5.5}
dict_parameters = {'a': 1.4, 'b': 5.5}

sum_list_parameters = sum(list_parameters)
sum_tuple_parameteres = sum(tuple_parameteres)
sum_set_parameters = sum(set_parameters)
sum_dict_parameters = dict_parameters['a'] + dict_parameters['b']

print('task1', '\n')

print('summs of 4 ways of calcilations are:', '\n',
      'summ funcion of list parameters:', sum_list_parameters, '\n',
      'summ funcion of tuple parameters:', sum_tuple_parameteres, '\n',
      'summ funcion of set parameters:', sum_set_parameters, '\n',
      'common summ with "+" operator for dicitonary elements:', sum_dict_parameters, '\n')
# как вывесьи надпись '+' вместо "+"?
# также появился пробел 1 пробел в начале всех строк послепервой, как его убрать?

# task 1.2

substraction_a_b = dict_parameters['a'] - dict_parameters['b']

print('substraction of parameters is:', substraction_a_b, '\n')

# task 1.3

multiplication_a_b = dict_parameters['a'] * dict_parameters['b']

print('multiplication of parameters is:', multiplication_a_b, '\n')

# task 2

print('task2', '\n')

x = -1.4
y = 2.7

result_x_y = (abs(x) - abs(y)) / (1 + abs(x * y))

print('the result is', result_x_y, '\n')

# task 3

print('task3', '\n')

cube_lenth = 4

print('the volume is', cube_lenth * cube_lenth * cube_lenth, '\n',
      'the square is', cube_lenth * cube_lenth, '\n')

# task 4

print('task4', '\n')

import math

a1 = 2.2
a2 = 3.3

print(
    'average a1 and a2 is', (a1 + a2) / 2, '\n'
                                           'geometric mean a1 and a2 is', math.sqrt(a1 * a2), '\n')

# task 5

print('task5', '\n')
cat_a = 1.4
cat_b = 5.4
print(
    'hyp_c is', math.sqrt(cat_a * cat_b) / 2, '\n'
                                              'square is', cat_a * cat_b / 2, '\n')
