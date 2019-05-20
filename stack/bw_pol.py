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
        elif token in ["+", "-", "/", "*"]:
            if len(stack) < 2:
                raise ValueError("Number expected. Wrong notation used")
            y = stack.pop()
            x = stack.pop()
            z = eval('{} {} {}'.format(x, token, y))
            stack.append(z)
        else:
            raise ValueError("Should only contain integers or operation string")
    if not stack:
        raise ValueError("Expression is empty: no value could be calculated")
    if not isinstance(stack[-1], int):
        raise ValueError("Number expected. Wrong notation used")
    if len(stack) > 1:
        raise ValueError("Unexpected token in stack. Wrong notation used")
    return stack.pop()

# TODO нужно разделить строку на составляющие токены — отдельный алгоритм, на выходе список токенов

# === Сортировочная станция Дейкстры ===

# определяем, является элемент числом или оператором
# если операнд (число) — сохраняем в итоговый список
# если оператор — сохраняем во внутренний стэк операторов
# каждый следующий оператор сравниваем с оператором в стэке
# задать приоритет выражений и понятие левой ассоциации (можно ли заменить это приоритетом?) 
# типа * > / > + > -

def shunting_yard(expression:list) -> list:
    """
    >>> A = shunting_yard([5, "+", 2])
    >>> print(A)
    [5, 2, '+']
    >>> A = shunting_yard([2, "+", 7, "*", 5])
    >>> print(A)
    [2, 7, 5, '*', '+']
    """
    output = []
    op_stack = []
    op_priority = {"-": 0, "+": 1, "/": 2, "*": 3}
    for token in expression:
        if isinstance(token, int):
            output.append(token)                                                 # все числа сразу кладём в результат
        if token in op_priority.keys():
            while op_stack and op_priority[op_stack[-1]] > op_priority[token]:   # если в стэке есть операторы с приоритетом выше, чем у следующего в выражении
                output.append(op_stack.pop())                                    # вынимает операторы из стэка в результат
            op_stack.append(token)                                               # потом кладём туда операторы с приоритетом ниже
    while op_stack:
        output.append(op_stack.pop())                                            # вынимаем оставшиеся операторы в результат
    return output





if __name__ == "__main__":
    import doctest
    doctest.testmod()