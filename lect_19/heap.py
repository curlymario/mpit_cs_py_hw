"""
Дерево — однонаправленный граф
Дерево в котором у каждого родителя не более двух прямых потомков — двоичное дерево
Глубина — вершины кратчайший путь от вершины до корня
Листья — вершины без потомков
Куча — двоичное дерево, у которого есть три свойства:
— в каждой вершине значение не больше, чем в потомках (или наоборот не меньше)
— глубина всех листьев отличается не больше чем на единицу
— куча заполняется слева направо без пробелов
     3
   /   \
  5     7
 / \   /
8  10 13

[3, 5, 7, 8, 10 13]
 0  1  2  3  4  5

заметим, что левый потомок имеет номер позиции родителя, умноженный на два + 1
а правый потомок номер позиции умножить на два + 2
j = i*2+1
g = i*2+2

узнать предка:
i = j-1 // 2
"""

# Релизация кучи по минимуму:

Class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size +=1
        self.shift_up(self, size-1)

    def shitf_up(self, i)
        while i != 0 and self.values[i] < self.values[(i-1)//2]:
            self.values[i], self.values[(i-1)//2] = self.values[(i-1)//2], self.values[i]

    def extract_min(self):
        if not self.size:
            return None
        min = self.values[0]
        self.values[0] = self.values.pop()
        self.size -= 1
        self.shif_down(0)
        return min

    def shift_down(self, i):
        while i*2 + 1 < self.size
            j = i
            if self.values[i*2 + 1] < self.values[i]:
                j = i*2 + 1
            if i*2 + 2 < self.size and self.values[i*2 + 2] < self.values[j]:
                j = i*2 + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]