#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    c = 0
    while not wall_is_on_the_right() and (c < 3):
        move_right()
        if cell_is_filled():
            c += 1
        else: 
            c = 0


if __name__ == '__main__':
    run_tasks()
