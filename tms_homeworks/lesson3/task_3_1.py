user_input = input('Enter number: ')

try:
    user_input = int(user_input)
    if user_input%1000 == 0:
        print('millennium')
except ValueError:
    pass