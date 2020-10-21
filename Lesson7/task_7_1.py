def inch_to_cm(inch):
    if isinstance(inch, float) or isinstance(inch, int):
        cm = inch * 2.54
        return cm
    else:
        print('Wrong input. Expected int or float type')
        return None


def cm_to_inch(cm):
    if isinstance(cm, float) or isinstance(cm, int):
        inch = cm / 2.54
        return inch
    else:
        print('Wrong input. Expected int or float type')
        return None


def mile_to_km(mile):
    if isinstance(mile, float) or isinstance(mile, int):
        km = mile * 1.60934
        return km
    else:
        print('Wrong input. Expected int or float type')
        return None


def km_to_mile(km):
    if isinstance(km, float) or isinstance(km, int):
        mile = km / 1.60934
        return mile
    else:
        print('Wrong input. Expected int or float type')
        return None


def pound_to_kg(pound):
    if isinstance(pound, float) or isinstance(pound, int):
        kg = pound * 2.20462
        return kg
        else:
            print('Wrong input. Expected int or float type')
            return None


def kg_to_pound(kg):
    if isinstance(kg, float) or isinstance(kg, int):
        pound = kg / 2.20462
        return pound
    else:
        print('Wrong input. Expected int or float type')
        return None


def ounce_to_gram(ounce):
    if isinstance(ounce, float) or isinstance(ounce, int):
        gram = ounce * 28.3495
        return gram
    else:
        print('Wrong input. Expected in or float type')
        return None


def gram_to_ounce(gram):
    if isinstance(gram, float) or isinstance(gram, int):
        ounce = gram / 28.3495
        return ounce
    else:
        print('Wrong input. Expected in or float type')
        return None


def gallon_to_liter(gallon):
    if isinstance(gallon, float) or isinstance(gallon, int):
        liter = gallon * 3.78541
        return liter
    else:
        print('Wrong input. Expected in or float type')
        return None


def liter_to_gallon(liter):
    if isinstance(liter, float) or isinstance(liter, int):
        gallon = liter / 3.78541
        return gallon
    else:
        print('Wrong input. Expected in or float type')
        return None


def pint_to_liter(pint):
    if isinstance(pint, float) or isinstance(pint, int):
        liter = pint / 2.11338
        return liter
    else:
        print('Wrong input. Expected in or float type')
        return None


def liter_to_pint(liter):
    if isinstance(liter, float) or isinstance(liter, int):
        pint = liter * 2.11338
        return pint
    else:
        print('Wrong input. Expected in or float type')
        return None


function_number_selected_by_user = None

# used to call functions as globals form strings
# tuple contains (function name, convert from arg, convert to arg)
convert_functions_dict = {
    '1': ('inch_to_cm', 'inches', 'centimeters'),
    '2': ('cm_to_inch', 'centimeters', 'inches'),
    '3': ('mile_to_km', 'miles', 'kilometers'),
    '4': ('km_to_mile', 'kilometers', 'miles'),
    '5': ('kg_to_pound', 'kilograms', 'pounds'),
    '6': ('pound_to_kg', 'pounds', 'kilograms'),
    '7': ('ounce_to_gram', 'ounces', 'grams'),
    '8': ('gram_to_ounce', 'grams', 'ounces'),
    '9': ('gallon_to_liter', 'gallons', 'liters'),
    '10': ('liter_to_gallon', 'liters', 'gallons'),
    '11': ('pint_to_liter', 'pints', 'liters'),
    '12': ('liter_to_pint', 'liters', 'pints')
}

number_of_functions = len(convert_functions_dict)

# generating message for user
functions_call_number_message = 'to convert: ' + '\n'
function_number = 0
for current_function_in_dict in convert_functions_dict.values():
    function_number += 1
    functions_call_number_message += (
        f''
        f'from '
        f'{current_function_in_dict[1]} '
        f'to '
        f'{current_function_in_dict[2]} '
        f'press '
        f'{function_number} '
        f'\n'
    )
functions_call_number_message += "enter '0' to quit"

while function_number_selected_by_user != '0':
    print(functions_call_number_message)
    function_number_selected_by_user = input('enter number: ')
    if (function_number_selected_by_user.isdigit() and
            int(function_number_selected_by_user) in range(1, number_of_functions + 1)):
        value_to_convert = input(
            f''
            f'Enter '
            f'{convert_functions_dict[function_number_selected_by_user][1]} '
            f'to convert to '
            f'{convert_functions_dict[function_number_selected_by_user][2]} '
            f''
        )
        if value_to_convert.replace('.', '', 1).isdigit():
            value_to_convert = float(value_to_convert)
            print(
                f''
                f'it is '
                f'{globals()[convert_functions_dict[function_number_selected_by_user][0]](value_to_convert)} '
                f'{convert_functions_dict[function_number_selected_by_user][2]} '
                f''
            )
        else:
            print('Expected integer or float')
            pass
    elif function_number_selected_by_user.isdigit() and int(function_number_selected_by_user) == 0:
        quit()
    else:
        print(f'expected numbers between 0 and {number_of_functions}')
    input('press enter to continue ')
    
    
 abracadabra
