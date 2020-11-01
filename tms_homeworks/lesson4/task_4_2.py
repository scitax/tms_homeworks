import random


#Generate 10 random numbers between 1 and 100
randomlist = random.sample(range(1, 100), 10)
print(f'The generated list is {randomlist}')

for_iterations = len(randomlist)
for_var = 0


# 1. while cycle
even_numbers_while_cycle= 0
for_var = 0
list_len = len(randomlist)
while for_var < list_len:
    if randomlist[for_var]%2 == 0:
        even_numbers_while_cycle+= 1
    for_var += 1

print(f'While cycle: The here are {even_numbers_while_cycle} even numbers in lis.')

# 2. for cycle
even_numbers_for_cycle = 0

for varinrange in randomlist:
    if varinrange%2 == 0:
        even_numbers_for_cycle += 1

print(f'For cycle: The here are {even_numbers_for_cycle} even numbers in lis.')

