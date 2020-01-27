# считываем граф, преобразуем его в матрицу смежности, которую храним в G
# отсутствие числа помечаем заведомо большим числом
# считаем, что n - количество вершин, вершины пронумерованы от 0
def simple_floid(G, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    return G

# Вам дано число N, далее N строк по N чисел - матрица смежности взвешенного графа, отсутствие ребра помечено как 0.
# На следующих двух строках даны 2 списка: с начальными вершинами и с целевыми вершинами.
# Вам необходимо распечатать таблицу кратчайших расстояний,
# где строки - список начальных вершин, а столбцы - список целевых вершин.


def main():
    N = read_number()
    G = read_graph(N)
    starts = [int(v) for v in input('Введи список начальных вершин: ').split()]
    ends = [int(v) for v in input('Введи список конечных вершин: ').split()]
    G = floid(G, N)
    ans = {start: {end: 0 for end in ends} for start in starts}
    for i in starts:
        for j in ends:
            ans[i][j] = G[i][j]
    print(ans)

def read_number():
    N = 0
    while not N:
        try:
            N = int(input('Введите число вершин больше ноля: '))
        except ValueError as e:
            print('Не получилось считать число, ошибка: ' + str(e) + ' Попробуйте ещё раз.')
    return N

def read_graph(N):
    print('Введи матрицу смежности')
    G = [[0]*N for i in range(N)]
    for i in range(N):
        G[i][:] = [int(v) for v in input().split()]
    return G

def floid(G, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    return G


if __name__ == "__main__":
    main()