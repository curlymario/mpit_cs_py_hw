def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

# из комментов с малым выделением памяти
def fib_light(n):
    left = 0
    right = 1
    for i in range(n):
        left, right = right, left
        right = left + right
    return right if n > 0 else left

# из лекции с занятием памяти
# fib = [0, 1] + [0]*(n - 1)
# for i in range (2, n+1):
#     fib[i] = fib[i -1] + fib[i - 2]
# return fib[n]
 
def count_trajectories(N):
    """ Кузнечик имеет два варианта хода: +1 и +2
        Функция возвращает, сколько есть траекторий пути от 1 до N
    """ 
    K = [0, 1] + [0]*(N-1) # у лектора было [0]*N
    for i in range(2, N+1):
        K[i] = K[i - 2] + K[i - 1]
    return K[N]

def count_allowed_trajectories(N:int, allowed:list):
    """ Варианты хода: +1, +2 и +3
        Запретим некоторые клетки
        Функция возвращает, сколько есть траекторий пути от 1 до N
    """ 
    K = [0, 1, int(allowed[2])] + [None]*(N-2) # у лектора было (N-3)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[N]

# price[i] - цена входа в клетку i
# cost[i] - минимально возможная суммарная стоимость достижения клетки i

def count_min_cost(N:int, price:list):
    """ Варианты хода: +1 и +2
    """ 
    cost = [None, price[1], price[1]+price[2]] + [0]*(N-2)
    for i in range(3, N+1):
        cost[i] = price[i] + min(cost[i-1], cost[i-2])
    return cost[N]


# == Лабораторная ==

def count_trajectories_3(N):
    """ Кузнечик имеет два варианта хода: +1, +2, +3
        Функция возвращает, сколько есть траекторий пути от 1 до N
    """ 
    K = [0, 1, 1] + [0]*(N-2) 
    for i in range(3, N+1):
        K[i] = K[i - 3] + K[i - 2] + K[i - 1]
    return K[N]

def count_trajectories_3(N):
    """ Кузнечик имеет два варианта хода: +1, +2, *3
        Функция возвращает, сколько есть траекторий пути от 1 до N
    """ 
    K = [0, 1, 1, 3] + [0]*(N-3) 
    for i in range(4, N+1):
        if i//3 == 0:
            K[i] = K[i/3] + K[i - 2] + K[i - 1]
        else:
            K[i] = K[i - 2] + K[i - 1]
    return K[N]

def calculate_min_cost(n, price):
    C = [0, price[1], price[1]+price[2]] + [0]*(n-2)
    for i in range(3, n+1):
        C[i] = min(C[i-1], C[i-2]) + price[i]
    return C[n]

def find_min_cost_route(n, price):
    C = [0, price[1], price[1]+price[2]] + [0]*(n-2)
    prev = [0, 1, 1]
    for i in range(3, n+1):
        if C[i-1] <= C[i-2]:
            C[i] = C[i-1] + price[i]
            prev.append(i - 1)
        else:   # C[i-2] < C[i-1]
            C[i] = C[i-2] + price[i]
            prev.append(i - 2)

    k = prev[-1]
    path = [n] + [k]
    while prev[k] != 1:
        path.append(prev[k])
        k = prev[k]
    path.append(1)
    path[:] = path[::-1]
    return(path)

# price = [1, 2, 4, 3, 2, 5, 6, 7, 3, 7, 8, 2, 8, 9, 1, 3, 2]
# n = len(price) - 1
# path = find_min_cost_route(n, price)
# print(path)