def function_args_reverse(in_function):
    def revers_args(*args):
        return in_function(args[::-1])
    return revers_args


@function_args_reverse
def any_func(*args):
    return args


print(any_func(1,2,3,4,5,6))

