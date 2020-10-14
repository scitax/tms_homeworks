import csv

def read_csv_file(filename: str) -> dict:
    """

    :param filename:
    :return: {'fields':[fields], 'rows': [rows]}
    """
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(filename)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    fields_rows_dict = {'fiels': fields, 'rows': rows, filename: str}
    return fields_rows_dict

def write_csv_file(filename: str, data_dict: dict):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data_dict['fields'])
        csvwriter.writerows(data_dict['rows'])

def add_new_row_to_csv(filename: str, row: list, pos: int = True):
    if pos:
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
    else:
        data_dict = read_csv_file(filename)
        row_data = data_dict['rows']
        row_data.insert(pos+1, row]
        data_dict['rows'] = row_data
        write_csv_file(filename, data_dict)


def dell_row_in_csv(filename: str, pos: int = True):
    data_dict = read_csv_file(filename)
    row_data = data_dict['rows']
    row_data.remove[pos + 1]
    data_dict['rows'] = row_data
    write_csv_file(filename, data_dict)
