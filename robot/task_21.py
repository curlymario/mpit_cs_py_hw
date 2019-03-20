#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for i in range(13):
        for j in range(i + 1):
            fill_cell()
            move_right()
        move_left(n = i + 1)
        move_down()


if __name__ == '__main__':
    run_tasks()
