# 1. while cycle
dict_hw = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

dict_len = len(dict_hw)
while_arg = 0

while while_arg < dict_len:
    temp_key = list(dict_hw)[0]
    new_key = temp_key + str(len(temp_key))
    dict_hw[new_key] = dict_hw[temp_key]
    del dict_hw[temp_key]
    while_arg += 1

print(f'While cycle: {dict_hw}')

# 2. for cycle

dict_hw = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

dict_hw = {x + str(len(x)): dict_hw[x] for x in dict_hw}

print(f'For cycle: {dict_hw}')
