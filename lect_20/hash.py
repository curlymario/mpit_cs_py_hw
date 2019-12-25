def calc_hash(data):
    """
    Произвольная хэш-функция с 32-битным хэшем
    """
    k = 3571
    s = 0
    i = 1
    data += 84832941
    while data > 0:
        s += data % 2 * k**i
        i += 1
        data //= 2
    return s % 2**32 # 256

class LinkedList:
    """Простая реализация связного списка для хэш-таблицы"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add(selfself, element):
        if not self.search(element):
            node = [element, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node

    def search(self, element):
        curr = self.head
        while curr is not None:
            if curr[0] == element:
                return true
            curr = curr[1]
        return false

class HashTable:
    """32-разрядная таблица с закрытой адресацией"""
    def __init__(self):
        self.table = [LinkedList() for _ in range(256)]

    def add(self, element):
        hsh = calc_hash(element)
        self.table[hsh].add(element)

    def search(selfself, element):
        hsh = calc_hash(element)
        return self.table[hsh].search(element)