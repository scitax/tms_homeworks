# 1. while cycle

list_hw = [1,2,3,4,5]
cycle_len = len(list_hw)
new_list = []
while_par = 1

while while_par < cycle_len:
    new_list.append(list_hw[while_par])
    while_par += 1
new_list.append(list_hw[0])

print(f'While cycle: {new_list}')


# 2. for cycle
for_count = 1
list_hw = [1,2,3,4,5]
new_list = []

for for_arg in list_hw:
    if for_count > 4:
        new_list.append(list_hw[0])
        break
    new_list.append(list_hw[for_count])
    for_count += 1

print(f'For cycle: {new_list}')