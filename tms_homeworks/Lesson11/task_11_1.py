import json


class Human:
    def __init__(self, age: int, name: str, surname: str):
        self.__age = age
        self.__name = name
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    def increase_age(self, age):
        self.__age += age

    def switch_name_surname(self):
        self.__surname, self.__name = self.__name, self.__surname


class Address:
    def __init__(self, address_line_1: str, address_line_2: str, city: str, zip_code: int):
        self.__address_line_1 = address_line_1
        self.__address_line_2 = address_line_2
        self.__city = city
        self.__zip_code = zip_code

    @property
    def address_line_1(self):
        return self.__address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        self.__address_line_1 = address_line_1

    @property
    def address_line_2(self):
        return self.__address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        self.__address_line_2 = address_line_2

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self.__zip_code = zip_code

    def return_data_in_json(self):
        json_data = json.dumps(
            {
                'address_line_1': self.__address_line_1,
                'address_line_2': self.__address_line_2,
                'city': self.__city,
                'zip_code': self.__zip_code
            }
        )
        return json_data

    def get_json_data(self, json_data: json):
        load_data = json.loads(json_data)
        self.__address_line_1 = load_data['address_line_1']
        self.__address_line_2 = load_data['address_line_2']
        self.__city = load_data['city']
        self.__zip_code = load_data['zip_code']



# class_3, class_4, class_5 = ctrl + C, ctrl + v
