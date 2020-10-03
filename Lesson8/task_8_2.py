from typing import Optional


def count_upper_lower_case(string_arg: Optional[str]) -> Optional[dict]:
    if not isinstance(string_arg, str):
        print('Error! String is expected')
        return None
    lower_upper_counter = {'lower': 0, 'upper': 0}
    for _ in string_arg:
        if _.islower():
            lower_upper_counter['lower'] += 1
        if _.isupper():
            lower_upper_counter['upper'] += 1
        else:
            pass
    return lower_upper_counter
