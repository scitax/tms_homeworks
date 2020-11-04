from datetime import datetime


def function_execution_time(function):
    def calc_execution_time(*args, **kwargs):
        time_before = datetime.now()
        function(*args, **kwargs)
        time_after = datetime.now()
        execution_time = time_after - time_before
        print(f'{function.__name__} execution time:')
        print(execution_time)
    return calc_execution_time


@function_execution_time
def range_cycle():
    for i in range(10000000):
        pass


@function_execution_time
def while_cycle():
    i = 0
    while i < 10000000:
        i += 1
        pass


# в какой-то из домашек было замечание, что for I in range (x) - выполняется дольше,
# while, потому что i бежит в range ищет там значение по индексу и тратит больше времени
# по факут in range работает быстрее. Лучше использоавть эту констукцию, или где-то ошибка?
while_cycle()
range_cycle()


