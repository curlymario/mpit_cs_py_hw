# ==== Сортировка слиянием ====

# Слияние отсортированных массивов
def merge(A:list, B:list):
    C = [0]*(len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:                # = для устойчивости сортировки
            C[n] = A[i]
            i += 1; n += 1
        else:
            C[n] = B[k]
            k += 1; n += 1
    while i < len(A):                   # залил остаток A или ничего, если A пустой
        C[n] = A[i]
        i += 1; n += 1
    while k < len(B):                   # залил остаток B или ничего, если B пустой
        C[n] = B[k]
        k += 1; n += 1
    return C

# Сортировка считается устойчивой, если она не меняет порядок равных элементов

# мой вариант с append вместо n
# def my_merge(A:list, B:list):
#     C = []
#     i = k = 0
#     while i < len(A) and k < len(B):
#         if A[i] <= B[k]:                # = для устойчивости сортировки
#             C.append(A[i])
#             i += 1
#         else:
#             C.append(B[k])
#             k += 1
#     C.append(*A[i:])                  # залил остаток A или ничего, если A пустой
#     C.append(*B[k:])                  # залил остаток B или ничего, если B пустой
#     return C
# Не корректно работает из-за особенностей работы append, надо думать

# A = [1,3,6,8,9]
# B = [0,2,4,5,7]

# print(merge(A, B))
# print(my_merge(A, B))


def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


# ==== Сортировка Тони Хоара (Quick Sort) ====
def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []              # можно сделать функционально и без использования памяти под L, M, R
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else: # x > barrier
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R: 
        A[k] = x
        k += 1

S = [1, 5, 7, 3, 6, 4, 8, 0, 9, 2]
merge_sort(S)
print(S)

S = [1, 5, 7, 3, 6, 4, 8, 0, 9, 2]
hoar_sort(S)
print(S)

def check_sorted(A, ascend=True):
    """ Проверяет упорядоченность массива A по возрастанию, если ascending=True
        или по убыванию, если ascending=False
        Алгоритм проверяет за O(len(A))
    """
    flag = True
    s = 2*int(ascend) - 1       # == 1 если ascend=True или -1 если ascend=False
    for i in range(0, len(A)-1):
        if s*A[i] > s*A[i+1]:   # s разворачивает знак при сортировке по убыванию
            flag = False
            break
    return flag


print(check_sorted(S))
