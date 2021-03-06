# Списки смежности на встроенных структуры python жрут много памяти

# Для фиксированных графов (неизменяемых, только для чтения) подойдут
# Компактные списки смежности
# отказываемся от хранения имён и 0
# Допустим такой граф
# 0: 1
# 1: 0, 2, 3
# 2: 1, 3
# 3: 1, 2, 4
# 4: 3
# сохраним в списке:
edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3] # а ещё лучше хранить в настоящих array битовые integer
# offset[i] начало списка смежности i-ой вершины
# offset[-1] — фиктивный оффсет для несуществующей вершины
offset = [0, 1, 4, 6, 9, 10]
# список смежности конкретной вершины:
edges[offset[i]:offset[i+1]]

# добавлять / удалять становится практически не применимо, зато очень удобно компактно хранить