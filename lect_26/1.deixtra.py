from collections import deque

def main():
    G = read_graph()
    start = input("С какой вершины начать?: ")
    while start not in G:
        start = input("Такой вершины в графе нет. С какой вершины начать?: ")
    shortest_distances = dijkstra(G, start)
    finish = input("К какой вершине построить путь?: ")
    while finish not in G:
        finish = input("Такой вершины в графе нет. К какой вершине построить путь?: ")
    shortest_path = restore_shortest_path(G, start, finish, shortest_distances)
    print(shortest_path)

def read_graph():
    M = int(input())    # Количество рёбер, строки "А Б вес"
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)

    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def dijkstra(G, start):
    Q = deque()     # очередь
    S = {}          # словарь кратчайших путей
    S[start] = 0
    Q.append(start)
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if (u not in S) or (S[v] + G[v][u] < S[u]):
                S[u] = S[v] + G[v][u]
                Q.append(u)
    return S

def restore_shortest_path(G, start, finish, shortest_distances):
    pass


if __name__ == "__main__":
    main()