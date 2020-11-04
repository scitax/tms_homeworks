guest_number = input('Укажите число гостей ')

try:
    guest_number = int(guest_number)
    if guest_number < 0:
        pass
# it is not clarified it TR what should happen if the number is 20 and 50
# 20 is included in condition for "дом", 50 is included in condition for "кафе"
# it is usually should be clarified by the product owner, but I'm to lazy to ask for it

    elif guest_number <= 20:
        print('дом')
    elif guest_number <= 50:
        print('кафе')
    elif guest_number > 50:
        print('ресторан')

except ValueError:
    pass