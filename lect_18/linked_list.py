# === Связный список ===

A = [1]
A.append([2]) # [1, [2]] — связный список
A[1].append([3, A]) # [1, [2, [3, A]]] — связное кольцо

A[1][1][1] = None # [1, [2, [3, None]]]

P = A
while P is not None:
    print(p[0])
    p = p[1]
# 1
# 2
# 3

# list() в Python — вектор, динамический массив ссылок

B = [0]*(10**6)
B.append() # O(1) если хватает резерва памяти или O(N) если не хватает
B.pop() # O(1)
B.insert(0, 1) # O(N) — от N+1 до 2*N+1 операций

class LinkedList:

    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, "list empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

    # __iter__ некогда добавлять, но тоже можно

a = LinkedList()
a.insert(5) # [5, None] — O(1)
a.insert(10) # [10, [5, None]]
a.pop() # 10 — O(2)
a.pop() # 5
# доступ к элементу односвязного списка a[i] — O(N)
