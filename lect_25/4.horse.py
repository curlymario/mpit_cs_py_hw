# Восстановление траектории шахматного коня

# 64 вершины
letters = 'abcdefgh'
numbers = '12345678'

graph = dict()
# создаём 64 именованные вершины (8×8)
for l in letters:
    for n in numbers:
        graph[l+n] = set()

def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

# ходим конём (1, 2) по клеткам, добавляем если такие клетки существуют на поле (
for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i+2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i-2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i+1] + numbers[j+2]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2  < 8:
            v2 = letters[i-1] + numbers[j+2]
            add_edge(v1, v2)
# не перебрали варианты для j-1 и j-2 для v1,
# потому что они наверняка будут перебраны из v2 по ходу прохождения по доске

from collections import deque

distances = {v: None for v in graph}
parents = {v: None for v in graph}

start_vertex = 'd4'
end_vertex = 'f7'

distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v)

path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parents = parents[parent]
