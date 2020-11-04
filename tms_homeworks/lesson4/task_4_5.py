consequence_hw_while = [1, 1]

# 1. while cycle
i = 1

while i < 14:
    next_arg = consequence_hw_while[i-1] + consequence_hw_while[i]
    i = i + 1
    consequence_hw_while.append(next_arg)

print(f'While cycle: {consequence_hw_while}')


# 2. for cycle
consequence_hw_for = [1, 1]

for arg_for in range(13):
    next_arg = consequence_hw_for[arg_for] + consequence_hw_for[arg_for+1]
    consequence_hw_for.append(next_arg)

print(f'For cycle: {consequence_hw_for}')
