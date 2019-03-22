# a = [1, 2, 3, 4, 5]
# for x in a:
#     print(x, type(x), type(a))
#     x += 1
#     print(x)

# A = [0] * 1000
# top = 0
# x = int(input())
# while x != 0:
#     A[top] = x
#     top += 1
#     x = int(input())
# print()
# for k in range((top - 1), -1, -1):
#     print(A[k])

# N = int(input())
# A = [0]*N
# B = [0]*N

# for k in range(N):
#     A[k] = int(input())
# for k in range(N):
#     B[k] = A[k]


# ==== Поиск в массиве ====

# def array_search(A:list, N:int, x:int):
#     """ Осуществляет поиск числа x в массиве A
#         от 0 до N-1 индекса включительно.
#         Возвращает индекс элемента x в массиве A
#         или -1, если такого нет.
#         Если в массиве несколько элементов равных x,
#         возвращает индекс первого по счёту
#     """
#     for k in range(N):
#         if A[k] == x:
#             return k
#     return -1

# def test_array_search():
#     A1 = [1, 2, 3, 4, 5]
#     m = array_search(A1, 5, 8)
#     if m == -1:
#         print('#test1 - ok')
#     else:
#         print('#test1 - fail')

#     A2 = [-1, -2, -3, -4, -5]
#     m = array_search(A2, 5, -3)
#     if m == 2:
#         print('#test2 - ok')
#     else:
#         print('#test2 - fail')

#     A3 = [10, 20, 30, 10, 10]
#     m = array_search(A3, 5, 10)
#     if m == 0:
#         print('#test3 - ok')
#     else:
#         print('#test3 - fail')

# test_array_search()


# ==== Обращение массива ====

# def invert_array(A, N):
#     """ Обращение массива (поворот задом наперёд)
#         в рамках индексов от 0 до N-1
#     """
#     for k in range(N//2):
#         A[k], A[N-1-k] = A[N-1-k], A[k]

# def test_invert_array():
#     A1 = [1, 2, 3, 4, 5]
#     print(A1)
#     invert_array(A1, 5)
#     print(A1)
#     if A1 == [5, 4, 3, 2, 1]:
#         print('#test1 - ok')
#     else:
#         print('#test1 - fail')

#     A2 = [0, 0, 0, 0, 0, 0, 0, 10]
#     print(A2)
#     invert_array(A2, 8)
#     print(A2)
#     if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
#         print('#test2 - ok')
#     else:
#         print('#test2 - fail')

# test_invert_array()


# ==== Циклический свдиг влево ====
def move_array_left(A, N):
    tmp = A[0]
    for k in range (N-1):
        A[k] = A[k+1]
    A[N-1] = tmp

# ==== Циклический свдиг вправо ====
def move_array_right(A, N):
    tmp = A[N-1]
    for k in range (N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp


# ==== Решето Эратосфена ====
def erathosphen(N):
    """ Находит все простые числа до N-1 включительно
    """
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]: 
            for m in range (2*k, N, k):
                A[m] = False
    for k in range(N):
        print(k, "—", "простое" if A[k] else "составное")
