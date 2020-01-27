import math

# Вам даны числа N и M, количество вершин и ребер ориентированного графа.
# Далее идет M строк вида u, v, w, где u и v задают начало и конец ребра, а w - его вес.
# В конце дано число - стартовая вершина.
# Теперь решите задачу из упражнения №2, реализовав алгоритм Дейкстры за O((N+M) log N).

def main():
    N, M = [int(x) for x in input('Введите размеры графа: ').split()]
    print('Введите рёбра графа:')
    graph = read_graph(M)
    start = int(input('Введите стартовую вершину: '))
    print(dijkstra(graph, start))

def dijkstra(graph, start):
    heap = Heap()
    d = {}
    d[start] = 0
    heap.insert(start)
    while heap.size > 0:
        v = heap.extract_min()
        for u in graph[v]:
            if (u not in d) or (d[v] + graph[v][u] < d[u]):
                d[u] = d[v] + graph[v][u]
                heap.insert(u)
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


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.shift_up(self.size-1)

    def shift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i-1)//2]:
            self.values[i], self.values[(i-1)//2] = self.values[(i-1)//2], self.values[i]

    def extract_min(self):
        if not self.size:
            return None
        min = self.values[0]
        self.values[0] = self.values.pop()
        self.size -= 1
        self.shift_down(0)
        return min

    def shift_down(self, i):
        while i*2 + 1 < self.size:
            j = i
            if self.values[i*2 + 1] < self.values[i]:
                j = i*2 + 1
            if i*2 + 2 < self.size and self.values[i*2 + 2] < self.values[j]:
                j = i*2 + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]

if __name__ == "__main__":
    main()