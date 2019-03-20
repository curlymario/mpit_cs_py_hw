#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    n = 0
    while wall_is_beneath():
        move_right()
        n += 1
    move_down()
    for i in range(n):
        move_left()



if __name__ == '__main__':
    run_tasks()
