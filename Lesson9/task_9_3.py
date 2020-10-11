def odd_filter_in_list(function_to_filter):
    def filtering_list_func(*args):
        filtered_list = []
        for int_in_lit in function_to_filter(*args):
            if not int_in_lit % 2 == 0:
                filtered_list.append(int_in_lit)
        print(filtered_list)
    return filtering_list_func


@odd_filter_in_list
def in_int_list(int_list: list) -> list:
    return int_list


in_int_list([1, 2, 3, 4, 5, 6, 7])