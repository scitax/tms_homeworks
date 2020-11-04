import random

#Generate 10 random numbers between 1 and 10
randomlist = random.sample(range(1, 11), 10)

print(f'primary list is: {randomlist}')

# 1. while cycle
randomlist_while_converted = []
for_iterations = len(randomlist)
for_var = 0

while for_var < for_iterations:
    randomlist_while_converted.append(randomlist[for_var] * -2)
    for_var += 1

print(f'converted list with while cycle: {randomlist_while_converted}')

# 2. for cycle
randomlist_for_converted = []

for varinrange in randomlist:
    randomlist_for_converted.append(varinrange*-2)

print(f'converted list with for cycle: {randomlist_for_converted}')
