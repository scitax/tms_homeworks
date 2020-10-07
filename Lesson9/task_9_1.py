from typing import Optional, List

some_list = ['Masha', 'Petia', 'Roma', 'Kira', 'Arina', 'Vasia', (1, 3), 'Olia', 'Vasia', 'Sahsa', (1, 3)]


# var 1
def format_list_v1(input_list: List[str]) -> List[str]:
    input_list = iter(input_list)
    counter = 0
    result_list = []
    for list_item in input_list:
        if not isinstance(list_item, str):
            print(f'№ {counter} item {list_item} in list is not a string')
            pass
        else:
            result_list.append(f'{counter} - {list_item}')
            counter += 1
    return result_list


# var 2. Just to show the usage of next function in the iter objects
def format_list_v2(input_list: List[str]) -> List[str]:
    input_list = iter(input_list)
    counter = 0
    result_list = []
    # it is possible to define input_list len and make cycle with it.
    # here is an example how to run throe the whole iter object
    try:
        while True:
            item_in_list = next(input_list)
            if not isinstance(item_in_list, str):
                print(f'№ {counter} item {item_in_list} in list is not a string')
                pass
            else:
                result_list.append(f'{counter} - {item_in_list}')
            counter += 1
    except StopIteration:
        return result_list


print(format_list_v2(some_list))
