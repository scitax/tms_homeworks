class Dog:
    def __init__(self, height, weight, name, age, master=None, address=None):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__address = address

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, height):
        self.__weight = weight
        return self.__weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return self.__name

    def locals_data(self):
        self.locals_date = locals()
        print(self.locals_date)




if __name__ =='__main__':
    action = Dog(10, 20, 'Abra', 5, '111')
    action.locals_data()
