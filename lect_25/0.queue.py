# Стек: last in, first out
# Очередь: first in, first out

# Медленная очередь — список
queue_slow = []
queue_slow.append(5)
queue_slow.append(10)
queue_slow.append(7)
print(queue_slow)   # [5, 10, 7]

x = queue_slow.pop(0) # O(N) по времени!
print(x)            # 5
print(queue_slow)   # [10, 7]

# Тяжёлая очередь
queue_big = list(range(100000000))
q_start = 0
# remove превращается в две операции
# мы не удаляем элемент из памяти, а просто сдвигаемся
x = queue_big[q_start]  # O(1)
q_start += 1            # O(1)
# быстро, но требует всегда держать резерв памяти занятым

# Наиболее эффективная — в библиотеке deque
from collection import deque
queue = deque(range(10000000))
queue.append(1)
x = queue.popleft()
# медленнее, чем предыдущее, но всё равно очень быстро
# можно написать самим через двусвязный список