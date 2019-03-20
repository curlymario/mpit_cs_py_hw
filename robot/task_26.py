#!/usr/bin/python3

from pyrob.api import *

def draw_cross():
    move_down()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_left()
    move_down()
    fill_cell()
    for i in range(2):
        move_up()
        fill_cell()
    move_left()

def draw_line_of_crosses(x):
    for i in range(x):
        draw_cross()
        if i < x - 1:
            move_right(n = 4)
    move_left(n = 4 * (x - 1))

@task(delay=0.02)
def task_2_4():
    for j in range(5):
        draw_line_of_crosses(10)
        if j < 4:
            move_down(n = 4)


if __name__ == '__main__':
    run_tasks()
