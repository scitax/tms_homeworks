import sqlite3
import os
from typing import List


class user_crud:
    def __init__(self, db_name: str):
        if not os.path.exists('db_log.txt'):
            os.mknod('db_log.txt')
        self.db_name = db_name
        self.connection = self._get_connection()
        self.cursor = self._get_cursor()
        self.CRATE_TABLE_QUERY = """
            CREATE TABLE user (
                id integer PRIMARY KEY AUTOINCREMENT,
                first_name varchar(255),
                last_name varchar(255)
                age integer
            )
        """
        self.insert_data_query = "INSERT INTO user (first_name, last_name, age) VALUES (?, ?, ?)"
        self.select_by_name_query = "SELECT * FROM user WHERE first_name = ?"
        self.select_below_25_query = "SELECT * FROM user WHERE age < 25"
        self.select_between_age_age_query = "SELECT * FROM user WHERE age >= ? AND age <= ?"


    def _get_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def _get_cursor(self):
        try:
            return self.connection.cursor()
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def create_table(self):
        try:
            return self.cursor.execute(self.CRATE_TABLE_QUERY)
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def insert_data(self, data_list: List[tuple]):
        try:
            return self.cursor.execute(self.insert_data_query, data_list)
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def select_by_name(self, name: str):
        try:
            return self.cursor.execute(self.select_by_name_query, name)
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def select_below_25(self):
        try:
            return self.cursor.execute(self.select_below_25_query)
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def select_between_age_age(self, *, min_age: int, max_age: int):
        try:
            return self.cursor.execute(self.select_between_age_age_query, (min_age, max_age))
        except sqlite3.Error as e:
            with open('log.txt', 'a') as file:
                file.write(str(e))

    def close_connection_cursor(self):
        self.cursor.close()
        self.connection.close()



if __name__ == '__main__':
    pass