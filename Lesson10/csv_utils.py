import csv
from typing import Dict, List, Optional


def read_csv_file(filename: str) -> Dict[str, list] or None:
    """
    //Зависит от задачи но здесь пустые строки не будут записываться. Для задачи можно было бы использовать
    dict_reader и dict_writer но напишем свои//

    :param filename:
    :return: {'fields':[fields], 'rows': [rows], 'columns': [columns]}
    """
    rows = []
    columns = []
    fields = []
    fields_rows_dict = {}
    trigger_for_rows = True

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if not row == []:
                if trigger_for_rows:
                    fields.append(row)
                    for _ in row:
                        columns.append([])
                    trigger_for_rows = False
                    continue
                rows.append(row)
                col_number = 0
                for column_data in row:
                    columns[col_number].append(column_data)
                    col_number += 1
    fields_rows_dict['fields'] = fields
    fields_rows_dict['rows'] = rows
    fields_rows_dict['columns'] = columns
    return fields_rows_dict


def write_csv_file(filename: str, data_dict: dict):
    """


    :param filename:
    :param data_dict = {'fields':[fields], 'rows': [rows]}:
    :return:
    """
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data_dict['fields'])
        csvwriter.writerows(data_dict['rows'])


def add_new_row_to_csv(filename: str, row: list, pos: int = True):
    if pos:
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
    else:
        data_dict = read_csv_file(filename)
        row_data = data_dict['rows']
        row_data.insert(pos, row)
        data_dict['rows'] = row_data
        write_csv_file(filename, data_dict)


def dell_row_in_csv(filename: str, pos: int):
    data_dict = read_csv_file(filename)
    row_data = data_dict['rows']
    row_data.pop(pos)
    data_dict['rows'] = row_data
    write_csv_file(filename, data_dict)
