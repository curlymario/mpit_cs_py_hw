import matplotlib
import random
import math
import util


def bubble_sort(a):
    for i in range(len(a), 1, -1):
        for k in range(0, i-1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]

def bubble_sort_adaptive(a):
    flag = True
    for i in range(len(a), 1, -1):
        if flag:
            flag = False
            for k in range(0, i-1):
                if a[k] > a[k+1]:
                    a[k], a[k+1] = a[k+1], a[k]
                    flag = True

util.plot_bubble_sort_results(
    ('Обычная реализация', bubble_sort),
    ('Реализация с проверкой на отсортированность', bubble_sort_adaptive)
)