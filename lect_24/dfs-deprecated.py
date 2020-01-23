def dfs(vertex, graph, used=None):
    # if used is None:
    #     used = set()
    used = used or set()
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)

used = {start}