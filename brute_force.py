def is_simple_num(x):
    """ Определяет, является ли число простым.
        x — челое, положительное число.
        Если простое, возвращает True,
        а иначе — False
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True

print(is_simple_num(4))
print(is_simple_num(19))

def factorize_num(x):
    """ Раскладывает число на множители
        Печатает их на экран
        x — целое положительное.
    """

    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1

factorize_num(999)
factorize_num(1024)
