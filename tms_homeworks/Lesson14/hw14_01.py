import argparse
import os
from time import sleep
from datetime import timedelta, datetime


class Tomato_timer_tools:
    @staticmethod
    def one_seconds_timer():
        while True:
            sleep(1)
            yield timedelta(seconds=1)

    @staticmethod
    def clear_console():
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')

    @staticmethod
    def create_file_if_not_exist():
        if not os.path.exists('focus_training_log.txt'):
            os.mknod('focus_training_log.txt')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-s', '--surname', required=True)
    parser.add_argument('-ft', '--focus-time', type=int, default=25, help='Minutes. By default = 25 min')
    parser.add_argument('-bt', '--brake-time', type=int, default=5, help='Minutes. By default = 5 min')
    parser.add_argument('-rt', '--repeat-times', type=int, default=4)
    parser.add_argument('-tn', '--task-name', required=True)
    args = parser.parse_args()

    focus_time = timedelta(minutes=args.focus_time)
    brake_time = timedelta(minutes=args.brake_time)
    zero_time = timedelta(0)
    repeat_times = args.repeat_times

    # creating log file if not exist
    if not os.path.exists('focus_training_log.txt'):
        os.mknod('focus_training_log.txt')

    # main body
    with open('focus_training_log.txt', 'a') as file_log:
        file_log.write(f'{datetime.now()} {args.task_name} by {args.name} {args.surname}')
        for current_repeat_time in range(1, repeat_times):
            time_left = focus_time
            # stopwatch and writing log for focus time
            for time_delta in Tomato_timer_tools.one_seconds_timer():
                Tomato_timer_tools.clear_console()
                print(f'{current_repeat_time} of {repeat_times} Training: {time_left} min')
                file_log.write(f'time_left')
                time_left -= time_delta
                # pause time
                if time_delta >= zero_time:
                    Tomato_timer_tools.clear_console()
                    print(f'{current_repeat_time} of {repeat_times} Break: {brake_time} min')
                    file_log.write(f'{current_repeat_time} of {repeat_times} Break')
                    sleep(60*args.brake_time)
                    break
