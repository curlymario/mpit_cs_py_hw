#  === Обратная польская нотация (алгоритм ОПН) ===
# Алгоритм вычисления арифметических выражений в постфиксной нотации
# [5, 2, "+"] ←→ 5 + 2
# (2 + 7) * 5 ←→ [2, 7, "+", 5, "*"]
# 2 + 7 * 5 ←→ [2, 7, 5, "*", "+"]
# Токен — число, символ
# Для каждого токен, если очередной токен — число — кладём его в стек
# Иначе он операция — берём из стека два операнда и вычисляем результат операции и кладём в стек
# Важно не перепутать левый и правый операнды, т.к. стек выдаёт их в обратном порядке
# y = stack.pop()
# x = stack.pop()
# z = x "операция" y
# stack.puzh(z)

# result = stack.pop()

# === Стековый калькулятор ===

def calc(expression:list):
    """ Takes an expression as a list of numbers and operations
    Calculates operations and returns final result as int
    TODO: exceptions and errors

    >>> calc([5, 2, "+"])
    7
    >>> calc([2, 7, "+", 5, "*"])
    45
    >>> calc([2, 7, 5, "*", "+"])
    37
    """
    stack = []
    for token in expression:
        if isinstance(token, int):
            stack.append(token)
        else:
            y = stack.pop()
            x = stack.pop()
            z = eval('{} {} {}'.format(x, token, y))
            stack.append(z)
    return stack.pop()





if __name__ == "__main__":
    import doctest
    doctest.testmod()