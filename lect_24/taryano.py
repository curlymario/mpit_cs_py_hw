# Топологическая сортировка. Алгоритм Тарьяно.
#
# Если ориентированный граф не содержит циклов,
# то его вершины можно пронумеровать так,
# что ребро от вершины с меньшим номером к вершине с большим номером
#
# Пример задачи: определить приоритет/порядок действий,
# чтобы несколько раз не возвращаться к предыдущим этапам
# чтобы не оказывалось что для этапа не выполнено условие на предыдущем
# (постройка дома, сбор документов, подписей и печатей, и т.д.)
#
# u - число от 1 до N

def dfs(start, graph, visited, answer):
    visited.[start] = True
    for u in graph[start]:
        if not visited[u]:
            dfs(u, graph, visited, answer)
    answer.append(start) # вся смысловая нагрузка здесь

visited = [False]*(N+1)
answer = []
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, graph, visited, answer)

answer[:] = answer[::-1]




def dfs2(start, graph, visited, answer):
    visited.[start] = True
    for u in graph[start]:
        if u not in visited:
            dfs(u, graph, visited, answer)
    answer.append(start)

visited2 = set()
answer2 = []
for vertex in graph:
    if vertex not in visited2
        dfs(vertex, graph, visited2, answer2)

answer2[:] = answer2[::-1]