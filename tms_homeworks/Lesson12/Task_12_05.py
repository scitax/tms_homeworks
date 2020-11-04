class Mytime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = (0,0,0)

    def __eq__(self, *args, **kwargs):
        return a == args

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

a = Mytime(1,2,3)
b = Mytime(1,2,3)

print(a.__dict__ == b.__dict__)