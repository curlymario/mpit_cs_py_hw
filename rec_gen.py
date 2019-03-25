# === Генератор всех цифр ===

def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")

# gen_bin(3)


def gen_nums(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-ричной системе счисления (N <= 10)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_nums(N, M-1, prefix)
        prefix.pop()

# gen_nums(4, 3)


# ==== Генератор всех перестановок чисел ====

def find_in(x, A):
    """ Ищет число x в A и возвращает True, если такой есть,
        False, если такого нет
    """
    for i in A:
        if x == i:
            return True
    return False

def gen_permuts(N:int, M:int=-1, prefix=None):
    """ Генерирует все перестановки N чисел
        в M позициях, с префиксом prefix
    """
    M = N if M == -1 else M # По умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep="", end=", ")
        return
    for number in range(1, N+1):
        # if find_in(number, prefix):
        if number in prefix:
            continue
        prefix.append(number)
        gen_permuts(N, M-1, prefix)
        prefix.pop()

gen_permuts(3)