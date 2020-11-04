from functools import reduce
from random import randint


def randomlist_gen(list_len, max_num):
    """
    :param list_len: - int, length of the returned list
    :param max_num: int
    :return: random_list[randint(0, max_num)....]
    """
    count = 0
    randomlist = []
    while count < list_len:
        rand_num = randint(0, max_num)
        randomlist.append(rand_num)
        count += 1
    return randomlist


random_list = randomlist_gen(4, 10)
print(random_list)
derivative = 3


converted_list_result = reduce(
    lambda x, y: x * (y ** int(y % derivative == 0)),
    random_list,
    1
)

print(converted_list_result)
