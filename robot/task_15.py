#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        while not wall_is_beneath():
            move_down()
    else:
        while not wall_is_above():
            move_up()

    if wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
    else:
        while not wall_is_on_the_left():
            move_left()

if __name__ == '__main__':
    run_tasks()
