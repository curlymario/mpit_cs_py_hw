# === Проверка корректности скобочной последовательности ===
# Корректные выражения:
# A = ""
# B = (A)
# C = AB
# Например "(()())" — корректное скобочное выражение
# "())(()" — некорректное скобочное выражение
# Если построем график незакрытых скобок, 
# у корректных выражений число незакрытых скобок не бывает ниже нуля
# т.о. нужно считать число незакрытых скобок
# общее количество незакрытых скобок n == 0
# по ходу последовательности n >= 0
# если вид скобок один, стэк не нужен, достаточно одной переменной n
# если два вида скобок:
# A = ""
# B = (A)
# B = [A]
# C = AB
# "[(())]([])" — корректная
# "[)" — некорректная
# проверка не сводится к графику n
# можно завести две переменные?
# "[(])" — все переменные равны 0 в конце, ни одна не уходит ниже 0 в процессе, но структура некорректная
# нужно помнить последнюю незакрытую скобку? недостаточно, если последовательность длинная
# нужно помнить все скобки, для этого применяется стэк

# == Алгоритм ==
# для очередной скобки
# если скобка открывающая,положить её в стек
# если скобка закрывалющая, то
# если стек пуст — некорректно
# иначе добываю скобку из стека
# и сравниваю скобку в стеке и очередную скобку
# если скобка из стека не соответствует очередной скобке — некорректно
# если после этого стек пуст, то корректно, иначе нет
# stack = []
# for i in range in len(A):
#     if A[i] == '(' or A[i] == '[':
#         stack.append(A[i])
#     else:
#         if len(stack) == 0:
#             return False
#         else:
#             x = stack.pop()
#             if A[i] == '(' and not x == ')' or A[i] == '[' and not x == ']':
#                 return False
# if len(stack) == 0:
#     return True
# else:
#     return False

import stackA

def is_braces_sequence_correct(s:str) -> bool:
    """ 
    Проверяет корректность скобочной последовательности 
    из круглых и квадратных скобок () и []

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("([]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct(")")
    False
    """
    for brace in s:
        if brace not in "()[]":
            continue    # игнорирование лишних символов
        if brace in "([":
            stackA.push(brace)
        else:
            assert brace in ")]", "Ожидалась закрывающая скобка: " + str(brace)
            if stackA.is_empty():
                return False
            left = stackA.pop()
            assert left in "([", "Ожидалась открывающая скобка: " + str(left)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            # else:
            #     raise Exception
            if right != brace:
                return False
    # if stackA.is_empty():
    #     return True
    # else:
    #     return False
    return stackA.is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)