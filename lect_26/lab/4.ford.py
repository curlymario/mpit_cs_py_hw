# Алгоритм Форда-Беллмана
# используется для поиска кратчайшего расстояния от одной вершины до остальных.
# Является типичным алгоритмом ДП.
# Состояния описываются двумя параметрами и означают
# "длину кратчайшего пути, проходящего не более, чем по i ребрам, и заканчивающегося в вершине j".

import math

def basic_ford_bellman(n, s, edges):
    # считываем граф, преобразуем его в список ребер, который храним в edges
    d = [None]*n  # Считаем, что n - кол-во вершин, вершины пронумерованы от 0
    d[s] = 0
    for i in range(n-1):
        for u, v, w in edges:
            if d[u] is not None:
                d[v] = min(math.inf if d[v] is None else d[v], d[u] + w)

# Решите задачу из упражнения №2, используя алгоритм Форда-Беллмана.
# Гарантируется, что циклов отрицательного веса в графе нет.

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
           elif d[v] is not None:
               d[u] = min(math.inf, d[v] + weight)
    return d

if __name__ == "__main__":
    main()