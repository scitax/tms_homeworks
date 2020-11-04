import argparse
import os
from time import sleep
from Task_12_1 import Mytime
from datetime import datetime


class Tomato_timer:
    usage_counter = 0

    def __init__(
            self,
            name: str,
            surname: str,
            focus_time: int = 25,
            breake_time: int = 5,
            sycle_no: int = 4,
            task_name: str = None
    ):
        self.name = name
        self.surname = surname
        self.focus_time = focus_time
        self.breake_time = breake_time
        self.sycle_no = sycle_no
        self.task_name = task_name
        Tomato_timer.usage_counter += 1

    @
    def ifinit_generator():
        while True:
            sleep(1)
            yield '0:0:1'


if __name__ == '__main__':
