#!/usr/bin/python3

from pyrob.api import *

def find_exit():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_beneath():
            break
    else:
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                break
        else:
            return True
    return False

@task(delay=0.01)
def task_8_30():
    dead_end = False
    while not dead_end:
        dead_end = find_exit()
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
