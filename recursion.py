# def matryoshka(n):
#     if n == 1:
#         print('Матрёшечка')
#     else:
#         print('Верх матрёшки n =', n)
#         matryoshka(n-1)
#         print('Низ матрёшки n = ', n)

# matryoshka(5)


# ==== Факториал ====
def factorial(n:int):
    assert n >= 0, "Факториал отрицательного не определён"
    if n == 0:
        return 1
    return factorial(n-1) * n


# ==== Алгоритм Евклида ====
def gcd(a:int, b:int):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:   # a < b
        return gcd(a, b-a)


# ==== Алгоритм Евклида на стероидах ====
def gcd_fast(a:int, b:int):
    return a if b == 0 else gcd_fast(b, a%b)
    # if b == 0:
    #     return a
    # return gcd_fast(b, a%b)


# ==== Быстрое возведение в степень ====
def pow(a:float, n:int):
    assert n >=0, "Возведение в отрицательную степень не реализовано"
    if n == 0:
        return 1
    else:
        return pow(a, n-1)*a


# ==== Быстрое возведение в степень на стероидах ====
def pow_fast(a:float, n:int):
    assert n >=0, "Возведение в отрицательную степень не реализовано"
    if n == 0:
        return 1
    elif n%2 == 1:  # нечёт
        return pow(a, n-1)*a
    else:           # чёт
        return pow(a**2, n//2)


# ==== Ханойские башни ====
# столбцы k, i, tmp
# k + i + tmp = 6
# tmp = 6 - k - i
# k содержит 1 блин размера n и n-1 блинов поменьше
# переложить n-1 блинов из k в tmp (рекурсия)
# переложить блин размера n из k в i
# переложить n-1 блинов из tmp в i (рекурсия)

def hanoi(n, x, y):
  if n > 0:
    for z in set([0,1,2]) - set([x,y]):
        hanoi(n-1, x, z)
        print(x, "->", y)
        hanoi(n-1, z, y)

n = int(input())
hanoi(n, 0, 2)