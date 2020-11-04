from csv_utils import write_csv_file, add_new_row_to_csv, \
    dell_row_in_csv
from random import randint

def generating_random_goods(number_of_rows:int):
    if not isinstance(number_of_rows, int):
        return None
    product_name = 'Name'
    product_price = 'Price'
    quantity = 'Quantity'
    comments = 'Comments'
    fields = [product_name, product_price, quantity, comments]
    rows = []
    goods_data = {'fields': fields}
    for row_number in range(1, number_of_rows + 1):
        product_name = f'product {row_number}'
        product_price = randint(10, 100)
        quantity = randint(0, 20)
        comments = f'comment {row_number}'
        rows.append([product_name, product_price, quantity, comments])
    goods_data['rows'] = rows
    return goods_data


random_godds_data = generating_random_goods(6)
file_name_for_hw = 'goods_data'

# writing random_godds_data to exel file: file_name_for_hw
write_csv_file(file_name_for_hw, random_godds_data)

new_possition = ['iPhone 12 Pro Max', 10000, 0, 'the best phone in the world']

# adding new_posion to exel file: file_name_for_hw
add_new_row_to_csv(file_name_for_hw, new_possition)

# deleting 2 row in exel file: file_name_for_hw
dell_row_in_csv(file_name_for_hw, 3)
