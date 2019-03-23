import turtle as t

t.speed('fastest')


# # ==== Факториал ====
# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n - 1)


# def fac_no_rec(n):
#     f = 1
#     x = 2
#     while x <= n:
#         f *= x
#         x += 1
#     return f

# import sys
# print(sys.getrecursionlimit())  # 1000
# print(fac(998))               # Recursion Error


# ==== Фибоначчи ====
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(7))
# print(fib(0))
# print(fib(25))


# ==== Фрактал ====
# def draw(l, n):
#     if n == 0:
#         t.left(180)
#         return
    
#     x = l / (n + 1)
#     for i in range(n):
#         t.forward(x)
#         t.left(45)
#         draw(0.5 * x * (n - i - 1), n - i - 1)
#         t.left(90)
#         draw(0.5 * x * (n - i - 1), n - i - 1)
#         t.right(135)
    
#     t.forward(x)
#     t.left(180)
#     t.forward(l)

# draw(400, 5)


# ==== Кривая Коха ====
def koch_line(x, n:int):
    """ Рисует кривую Коха длиной x с глубиной рекурсии n 
        На уровне 0 рисует горизонтальную прямую линию   
    """
    if n == 0:
        t.forward(x)
    else:
        koch_line(x/3, n-1)
        t.left(60)
        koch_line(x/3, n-1)
        t.right(120)
        koch_line(x/3, n-1)
        t.left(60)
        koch_line(x/3, n-1)

# koch_line(300, 4)


# ==== Снежинка Коха ====
def snowflake(x, n):
    """ Рисует снежинку Коха с длиной стороны x с глубиной рекурсии n 
        На уровне 0 рисует равносторонний треугольник
    """
    koch_line(x, n)
    t.right(120)
    koch_line(x, n)
    t.right(120)
    koch_line(x, n)
    t.right(120)

# snowflake(300, 3)


# ==== кривая Минковского ====
def mink_line(x, n:int):
    """ Рисует кривую Минковского длиной x с глубиной рекурсии n 
        На уровне 0 рисует горизонтальную прямую линию
    """
    if n == 0:
        t.forward(x)
    else:
        mink_line(x/4, n-1)
        t.left(90)
        mink_line(x/4, n-1)
        t.right(90)
        mink_line(x/4, n-1)
        t.right(90)
        mink_line(x/4, n-1)
        mink_line(x/4, n-1)
        t.left(90)
        mink_line(x/4, n-1)
        t.left(90)
        mink_line(x/4, n-1)
        t.right(90)
        mink_line(x/4, n-1)

# mink_line(200, 3)


# ==== Кривая Леви ====
def levi(x, n):
    if n == 0:
        t.forward(x)
    else:
        t.left(45)
        levi(0.75*x, n-1)
        t.right(90)
        levi(0.75*x, n-1)
        t.left(45)

# levi(100, 9)


# ==== Кривая дракона ====
def dragon(x, n, turn=False):
    if n == 0:
        t.forward(x)
    elif not turn:  # False
        t.right(45)
        dragon(x*0.75, n-1, False)
        t.left(90)
        dragon(x*0.75, n-1, True)
        t.right(45)
    else:           # True
        t.left(45)
        dragon(x*0.75, n-1, False)
        t.right(90)
        dragon(x*0.75, n-1, True)
        t.left(45)

# dragon(100, 20)


# ==== Канторово множество ====
def kantor(x, n):
    if n == 0:
        t.pendown()
        t.forward(x)
        t.penup()
    else:
        t.pendown()
        t.forward(x)
        t.penup()
        t.backward(x)
        t.right(90)
        t.forward(20)
        t.left(90)
        kantor(x/3, n-1)
        t.forward(x/3)
        kantor(x/3, n-1)
        t.left(90)
        t.forward(20)
        t.right(90)
        
kantor(300, 5)