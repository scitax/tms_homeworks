def some_gen(some_iter_obj) -> object:
    counter = 1
    for i in some_iter_obj:
        yield i
        counter += 1
        print(i)
print(next(getattr(('1','2','3'))))


result = map(lambda y, x, z: f'{str(x)}{str(y)}{str(z)}', [1, 2, 3, 4, 5, 6, 7, 8], ['a', 'b', 'c', 'd', 'e', 'f'],
             [1, 2, 3, 4, 5, 6, 7, 8])
print(type(result))

name_list = ['Masha', 'Petia', 'Roma', 'Kira', 'Arina', 'Vasia', 'Olia', 'Vasia', 'Sahsa']
result1 = filter(lambda x: 'k' in x.lower() if isinstance(x, str) else None, name_list)
print(list(result1))
