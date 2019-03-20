#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    s = 0
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        for i in range(s):
            if not wall_is_on_the_right():
                move_right()
        s += 1



if __name__ == '__main__':
    run_tasks()
