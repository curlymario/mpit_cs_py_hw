from collections import deque

N, M = map(int, input().split()) # считываем размеры графа
graph = {i: set() for i in range(N)} # dict comprehension по ключу на каждую вершину
for i in range(M):
    v1, v2 = map(int, input().split()) # считываем ребро
    graph[v1].add(v2)           # добавляем смежность двух вершин
    graph[v2].add(v1)

distances = [None] * N          # массив расстояний, по умолчанию неизвестны
start_vertex = 0                # начинаем с 0 вершины
distances[start_vertex] = 0
queue = deque([start_vertex])   # создаём очередь

parents = [None] * N # храним родителей

while queue:
    cur_v = queue.popleft()             # достаём первый элемент
    for neigh_v in graph[cur_v]:        # проходим всех его соседей
        if distances[neigh_v] is None:   # если сосед ещё не посещён
            distances[neigh_v] = distances[cur_v] + 1 # считываем расстояние
            parents[neigh_v] = cur_v    # запоминаем, откуда пришли в соседа
            queue.append(neigh_v)       # добавляем в очередь соседа, чтобы проверить и его соседей

print(distances)
print(parents)

# восстанавливаем путь до вершины 9
end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:       # ищем родителей родителей, пока они есть, чтобы найтипуть _от_ вершины
    path.append(parent)
    parents = parents[parent]

print(path[::-1])    # разворачиваем список, чтобы найти путь _до_ вершины