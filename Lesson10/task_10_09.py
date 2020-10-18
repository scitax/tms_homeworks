from csv_utils import read_csv_file, dell_row_in_csv, add_new_row_to_csv


file_name_for_hw = 'goods_data'
price_column_number = 1
product_quantity_column_number = 2


def calc_sum(filename: str, price_column_number: int, product_quantity_column_number: int):
    scv_data_from_file = read_csv_file(filename)
    rows_data = scv_data_from_file['rows']
    total_price = 0
    for product_data in rows_data:
        current_price = product_data[price_column_number]
        current_quantity = product_data[product_quantity_column_number]
        if current_price.isdigit() and current_quantity.isdigit():
            total_price += current_price*current_quantity
    return total_price


def calc_max_price(filename: str, price_column_number: int):
    scv_data_from_file = read_csv_file(filename)
    price_data = scv_data_from_file['columns'][price_column_number]
    product_data = scv_data_from_file['rows']
    max_price = price_data[0]
    max_price_products = []
    row_counter = 0
    for current_price in price_data:
        if current_price.isdigit():
            if current_price == max_price:
                max_price_products.append(product_data[row_counter])
            if current_price > max_price:
                max_price = current_price
                max_price_products.clear()
                max_price_products.append(product_data[row_counter])
        row_counter += 1
    return max_price_products

def calc_min_price(filename: str, price_column_number: int):
    scv_data_from_file = read_csv_file(filename)
    price_data = scv_data_from_file['columns'][price_column_number]
    product_data = scv_data_from_file['rows']
    min_price = price_data[0]
    max_price_products = []
    row_counter = 0
    for current_price in price_data:
        if current_price.isdigit():
            if current_price == min_price:
                max_price_products.append(product_data[row_counter])
            if current_price < min_price:
                min_price = current_price
                max_price_products.clear()
                max_price_products.append(product_data[row_counter])
        row_counter += 1
    return max_price_products

def changing_amoun_of_product(filename: str, product_quantity_column_number: int,
                              product_row_number: int, decrease_quantity: int = 1):
    scv_data_from_file = read_csv_file(filename)
    product_data = scv_data_from_file['rows'][product_row_number]
    quantity = product_data[product_quantity_column_number]
    if not quantity.isdigit():
        return None
    new_quantity = quantity - decrease_quantity
    product_data[product_quantity_column_number] = new_quantity
    dell_row_in_csv(file_name_for_hw, product_row_number)
    add_new_row_to_csv(file_name_for_hw, product_data, product_row_number)


