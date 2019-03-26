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
fib = [0, 1] + [0]*(n - 1)
for i in range (2, n+1):
    fib[i] = fib[i -1] + fib[i - 2]
# return fib[n]
 
def count_trajectories(N):
    """ Кузнечик имеет два варианта хода: +1 и +2
        Функция возвращает, сколько есть траекторий пути от 1 до N
    """ 
    K = [0, 1] + [0]*(N-1) # у лектора было [0]*N
    for i in range(2, N+1):
        K[i] = K[i - 2] + K[i -1]
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