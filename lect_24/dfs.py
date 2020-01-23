def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)

# поиск компонент связности:
used = set()
N = 0
for vertex in graph:
    if vertex not in used:
        dfs(vertex, G, used)
        N+=1
print(N)