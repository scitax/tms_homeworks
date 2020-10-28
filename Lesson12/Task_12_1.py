class Mytime:
    def __init__(self, *args):
        '''
        :param args:
            str: hrs:int, min:int, sec:int or str: 'hrs:min:sec' or Mytime object
        '''
        args_len = len(args)
        if args_len == 3:
            self.hours, self.minutes, self.seconds = args
            self.time_format()
        elif args_len == 1:
            in_arg = args[1]
            try:
                if isinstance(in_arg, Mytime):
                    self.hours = in_arg.hours
                    self.minutes = in_arg.minutes
                    self.seconds = in_arg.seconds
                    self.time_format()
            except:
                pass
            if isinstance(in_arg, str):
                time_list = in_arg.split(':')
                if len(time_list) == 3:
                    self.hours, self.minutes, self.seconds = map(int, time_list)
                    self.time_format()
        else:
            self.hours, self.minutes, self.seconds = (0, 0, 0)

    def time_format(self):
        min_sec_capacity = 60
        if abs(self.seconds) > 60:
            min_reminder = self.seconds // min_sec_capacity
            self.seconds = self.seconds % min_sec_capacity
            self.minutes += min_reminder
        if abs(self.minutes) > 60:
            hrs_reminder = self.minutes // min_sec_capacity
            self.minutes = self.minutes % min_sec_capacity
            self.hours += hrs_reminder

    def __eq__(self, other):
        return all([self.hours == other.hours, self.minutes == other.minutes, self.seconds == other.seconds])

    def __ne__(self, other):
        return all([self.hours != other.hours, self.minutes != other.minutes, self.seconds != other.seconds])

    def __lt__(self, other):
        return all([self.hours < other.hours, self.minutes < other.minutes, self.seconds < other.seconds])

    def __gt__(self, other):
        return all([self.hours > other.hours, self.minutes > other.minutes, self.seconds > other.seconds])

    def __le__(self, other):
        return all([self.hours <= other.hours, self.minutes <= other.minutes, self.seconds <= other.seconds])

    def __ge__(self, other):
        return all([self.hours >= other.hours, self.minutes >= other.minutes, self.seconds >= other.seconds])

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.hours
        self.seconds += other.seconds
        self.time_format()

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.hours
        self.seconds -= other.seconds
        self.time_format()

    def __mul__(self, other):
        if isinstance(other, int):
            self.hours *= other
            self.minutes *= other
            self.seconds *= other
            self.time_format()

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
