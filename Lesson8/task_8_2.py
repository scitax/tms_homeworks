from typing import Optional


def count_upper_lower_case(string_arg: Optional[str]) -> Optional[dict]:
    if not isinstance(string_arg, str):
        print('Error! String is expected')
        return None
    lower_case_count = 0
    upper_case_count = 0
    lower_upper_counter = {}
    for current_letter in string_arg:
        if current_letter.islower():
            lower_case_count += 1
        if current_letter.isupper():
            upper_case_count += 1
        else:
            pass
    lower_upper_counter['lower'] = lower_case_count
    lower_upper_counter['upper'] = upper_case_count
    return lower_upper_counter
