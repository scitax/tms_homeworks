from typing import Optional


def make_list_of_unique_values(primary_list: Optional[list]) -> Optional[list]:
    try:
        list_of_unique_values = list(set(primary_list))
        return list_of_unique_values
    except TypeError:
        print('Expected list or str type')
        return None

