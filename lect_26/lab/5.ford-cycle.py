import math

# Как и в предыдущих задачах, нам задан ориентированный взвешенный граф.
# Но теперь в нем могут быть циклы отрицательного веса. Необходимо вывести любой из таких циклов,
# либо сказать, что в графе его нет.

def main():
    N, M = [int(x) for x in input('Введите размеры графа: ').split()]
    print('Введите рёбра графа:')
    edges = read_edges(M)
    start = int(input('Введите стартовую вершину: '))
    print(ford(edges, start, N))

def read_edges(M):
    edges = [None]*M
    for i in range(M):
        a, b, weight = input().split()
        edges[i] = (int(a), int(b), float(weight))
    return edges

def ford(edges, start, N):
    d = [None]*N
    d[start] = 0
    for i in range(N-1):
       for u, v, weight in edges:
           if d[u] is not None:
               d[v] = min(math.inf if d[v] is None else d[v], d[u] + weight)
    cycle = []
    for u, v, weight in edges:
        dv_old = d[v]
        d[v] = min(d[v], d[u] + weight)
        if dv_old != d[v]:
            cycle.append((u, v, weight))

    if cycle:
        print("Цикл: " + str(cycle))
    else:
        print("Циклов нет")
    return d

if __name__ == "__main__":
    main()