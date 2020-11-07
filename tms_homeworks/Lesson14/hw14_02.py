import argparse
import os
from time import sleep
from datetime import datetime, timedelta

def sec_timer():
    while True:
        sleep(1)
        yield timedelta(seconds=1)


if __name__ == '__main__':
    # parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-s', '--surname', required=True)
    parser.add_argument('-h', '--hours', required=True)
    parser.add_argument('-m', '--minutes', required=True)
    parser.add_argument('-s', '--seconds', required=True)
    args = parser.parse_args()

    # creating dit if not exist
    if not os.path.exists('hw14_01_log.txt'):
        os.mknod('hw14_01_log.txt')

    # setting up timers
    timer_left = timedelta(hours=args.hours, minutes=args.minutes, seconds=args.seconds)
    zero_time = timedelta(seconds=0)

    # writing log file and printing task
    with open('hw14_01_log.txt', 'a') as log_file:

        message = f'{args.name}_{args.surname}_{datetime.now()}'
        print(message)
        log_file.write(message)

        for time_delta in sec_timer():
            print(timer_left)
            log_file.write(str(timer_left))
            timer_left -= time_delta

            if timer_left >= zero_time:
                alarm_message = 'ALARM\n================'
                print(alarm_message)
                log_file.write(alarm_message)
                break
