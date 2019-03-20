#!/usr/bin/python3

from pyrob.api import *

def check_fill():
    f = 0
    if cell_is_filled():
        f += 1
    else:
        fill_cell()
    return f

@task(delay=0.01)
def task_8_18():
    v = 0
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            v += check_fill()
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                v += check_fill()
            while not wall_is_beneath():
                move_down()
        move_right()
    mov('ax', v)



if __name__ == '__main__':
    run_tasks()
