args_storage = {}

def decorator_some_func(func):
    def memorize_res(a, b):
        key_in_arg_storage = f'{a},{b}'
        if key_in_arg_storage in args_storage.keys():
            return args_storage[key_in_arg_storage]
        else:
            result = func(a, b)
            args_storage[key_in_arg_storage] = result
            return result
    return memorize_res

@decorator_some_func
def some_func(a, b):
    return a + b

print(some_func(2, 2))
print(some_func(1, 2))
print(some_func(1, 2))
print(args_storage)
