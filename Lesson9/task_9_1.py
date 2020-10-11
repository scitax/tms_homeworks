from typing import Optional, List

some_list = ['Masha', 'Petia', 'Roma', 'Kira', 'Arina', 'Vasia', (1, 3), 'Olia', 'Vasia', 'Sahsa', (1, 3)]


def format_list(input_list: List[str]) -> List[str]:
    """
    :param input_list: args = [{value},...]
    :return: out_list: new args = ['{number} - {value}',...] number = value number in input_list
    """
    out_list = [f'{number} - {value}' for number, value in enumerate(input_list)]
    return out_list
