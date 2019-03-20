#!/usr/bin/python3

from pyrob.api import *


def draw_line():
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
    while not wall_is_on_the_left():
        move_left()

@task
def task_5_10():
    
    while not wall_is_beneath():
        draw_line()
        move_down()
    draw_line()

if __name__ == '__main__':
    run_tasks()
