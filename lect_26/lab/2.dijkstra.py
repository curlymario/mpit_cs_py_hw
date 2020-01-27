import math

# считываем граф, преобразуем его в список смежности, который храним в graph
def basic_dijkstra(graph, start, n):
    d = [math.inf]*n
    d[start] = 0
    used = [False]*n
    while True:
        u = -1
        for i in range(n):      # ищем вершину с наименьшим весом
            if not used[i] and (u == -1 or d[u] > d[i]):
                u = i
        if u == -1:
            break
        used[u] = True
        for v, w in graph[u]:   # улучшаем расстояния до всех смежных вершин
            d[v] = min(d[v], d[u] + w)
    return d

# Вам даны числа N и M, количество вершин и ребер ориентированного графа.
# Далее идет M строк вида u, v, w, где u и v задают начало и конец ребра, а w - его вес.
# В конце дано число - стартовая вершина.
# Посчитайте кратчайшие расстояния до всех вершин, используя алгоритм Дейкстры за O(N^2).

def main():
    N, M = [int(x) for x in input('Введите размеры графа: ').split()]
    print('Введите рёбра графа:')
    graph = read_graph(M)
    start = int(input('Введите стартовую вершину: '))
    print(dijkstra(graph, start, N))

def dijkstra(graph, start, N):
    d = {i: math.inf for i in range(N)}
    d[start] = 0
    used = [False]*N
    while True:
        u = -1
        for i in range(N):
            if not used[i] and (u == -1 or d[u] > d[i]):
                u = i
        if u == -1:
            break
        used[u] = True
        for v in graph[u]:
            d[v] = min(d[v], d[u] + graph[u][v])
    return d

def read_graph(M):
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        a, b = int(a), int(b)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {}
    G[a][b] = weight


if __name__ == "__main__":
    main()