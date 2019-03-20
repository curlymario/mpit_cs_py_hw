#!/usr/bin/python3

from pyrob.api import *


def paint_if_wall():
    if wall_is_above() and wall_is_beneath():
        fill_cell()

@task
def task_8_4():
    while not wall_is_on_the_right():
        paint_if_wall()
        move_right()
    paint_if_wall()
    


if __name__ == '__main__':
    run_tasks()
