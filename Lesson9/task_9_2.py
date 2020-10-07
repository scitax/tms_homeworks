double_keys = lambda **kwargs: {
    key_in_func * 2: kwargs[key_in_func]
    for key_in_func in kwargs
}
