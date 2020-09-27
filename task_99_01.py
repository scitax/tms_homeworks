# 1 variant cutting ***** string
star_string = '*****'
print('first variant result')
# printing first 5 lines
for temp_value in range(1, 6):
    print(star_string[:temp_value:])
# printing last 4 lines
for temp_value in range(1, 5):
    print(star_string[temp_value::])
print('\n')

# 2 variant creating stars '*' srting in cycle using end
print('second variant result')
# printing first 5 lines
for first_cycle_variable in range(0, 5):
    for second_cycle_variable in range(0, first_cycle_variable):
        print(end='*')
    print('*')
# printing last 4 lines
for first_cycle_variable in range(0, 4):
    for second_cycle_variable in range(0, 3 - first_cycle_variable):
        print(end='*')
    print('*')