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

@task
def task_2_1():
    move_right()
    move_down()
    draw_cross()



if __name__ == '__main__':
    run_tasks()
