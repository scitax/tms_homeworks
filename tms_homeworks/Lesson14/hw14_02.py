import argparse
import os
from time import sleep
from Task_12_1 import Mytime
from datetime import datetime

def ifinit_generator():
    while True:
        sleep(1)
        yield None


if __name__ == '__main__':
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)

    # parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-s', '--surname', required=True)
    parser.add_argument('-h', '--hours', required=True)
    parser.add_argument('-m', '--minutes', required=True)
    parser.add_argument('-s', '--seconds', required=True)
    args = parser.parse_args()

    time_object = Mytime(f'{args.hours}:{args.minutes}:{args.minutes}')

    if not os.path.exists('hw14_01_log.txt'):
        os.mknod('hw14_01_log.txt')

    with open('hw14_01_log.txt', 'a') as log_file:
        log_file.write(f'{args.name}_{args.surname}_{datetime.now()}')
        for time_delta in ifinit_generator():
            log_file.write(str(time_object))
            time_object -= time_delta
            if time_object.hours == time_object.minutes == time_object.seconds == 0:
                log_file.write('ALARM\n')
                break
