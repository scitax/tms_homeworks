class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    def run(self):
        pass

    def birthday(self):
        self.age += 1

    def sleep(self):
        pass

    def change_weight(self, diff=0.2):
        self.weight += diff

    def change_height(self, diff=0.2):
        self.height += diff

    def jump(self, jump_height):
        print(f'Jump {jump_height} meters')

    def voice(self):



class Dog(Pet):

    def jump(self, jump_height):
        if jump_height > 0.5:
            print('Dogs cannot jump so high')
        else:
            print(f'Jump {jump_height} meters')




class Cat(Pet):

    def jump(self, jump_height):
        if jump_height > 0.5:
            print(f'{self.__name__} cannot jump so high')
        print(f'Jump {jump_height} meters')




class Parrot(Pet):

    def __init__(self, species: str, can_speak: bool = False, *args, **kwargs):
        super(Parrot, self).__init__(*args, **kwargs)
        self.can_speak = can_speak
        self.species = species


    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly.')
        else:
            print('Fly!')

    def jump(self, jump_height):
        if jump_height > 0.05:
            print(f'{self.__name__} cannot jump so high')
        else:
            print(f'Jump {jump_height} meters')


def call_voice(*args: Pet):
    for animal in args:
        animal.voice()


if __name__ == '__main__'
    dog1 = Dog(1,2,3,4,5)
    cat1 = Cat(1,2,3,4,5)
    parrot = Parrot('1', True, 2,3,4,6)
    call_voice(dog1,cat1,parrot)

