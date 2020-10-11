double_keys_1 = lambda **kwargs: {
    f'{key_in_func}{key_in_func}': kwargs[key_in_func]
    for key_in_func in kwargs
}

double_keys_2 = lambda **kwargs: {
    f'{key_in_func}*2': arg_in_func
    for key_in_func, arg_in_func in kwargs.items()
}
