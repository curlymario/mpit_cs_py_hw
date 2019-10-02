# ========== Добродушные соседи ===========

# На ввод подается файл input.txt, в котором
# в первой строке записано три числа через пробел
# N - номер квартиры Фёдора,
# M - номер квартиры от которой Федор нашел ключи,
# K - ключ от этой квартиры.
# Далее i-я строка хранит описание ключей запертых в i-й квартире
# в формате <m_i0 - номер квартиры> <k_i0 - ключ>,<m_i1 - номер квартиры> <k_i1 - ключ>,... ,
# причем реальные номера квартир "зашифрованы" ключем от i-й квартиры(Ki) и находятся по формуле
# m_ij' = m_ij - Ki.
# Номера квартир начинаются с 0 (кпримеру вторая строка файла соответствует 0-й квартире).

# Нужно вывести ключ от квартиры Федора или None если его найти не получилось.

# Подсказка: используйте словарь для хранения ключей от еще не открытых комнат и множество для уже проверенных комнат.

import os


def import_text(rel_path) -> list:
    """ Ввести из файла список строк
        Вводим текст из файла (относительный адрес)
        Выдаём строку
    >>> import_text('test_file_2.txt')
    ['text, some text', '', 'some other text']
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, rel_path)
    file = open(file_path, "rt", encoding="utf-8")
    text = file.read().split("\n")

    return text


def import_initial_key(data_list) -> tuple:
    """ Извлечь из списка данные о квартире Фёдора и имеющийся ключ
        сохранить как массив (tuple) чисел (int)
    >>> A = ['4 0 1', '1 1,2 0,3 1,4 0', '3 0']
    >>> import_initial_key(A)
    (4, 0, 1)
    """
    key_line = data_list.pop(0)
    key_list = key_line.split()
    key_tuple = tuple(int(x) for x in key_list)

    return key_tuple


def import_apartments(apts_list) -> dict:
    """ Извлечь из списка данные о квартирах соседей
    >>> A = ['1 1,2 0,3 1,4 0', '3 0', '5 1,6 0', '',]
    >>> import_apartments(A)
    {0: [(1, 1), (2, 0), (3, 1), (4, 0)], 1: [(3, 0)], 2: [(5, 1), (6, 0)], 3: None}
    """
    i = 0
    apts_table = dict()
    for apt in apts_list:
        if apt == '':
            apts_table[i] = None
        else:
            apts_table[i] = []
            for key_pair in apt.split(','):
                m, k = key_pair.split()
                apts_table[i].append((int(m), int(k)))
        i += 1
    return apts_table


def find_key(text_file):
    """ Пройтись по квартирам и найти ключ
    >>> find_key('fedor.txt')
    1
    """
    data_list = import_text(text_file)
    fedor_apt, base_apt, base_key = import_initial_key(data_list)
    apt_table = import_apartments(data_list)

    current_apt, current_key = base_apt, base_key

    unlocked_apts = [None] * len(apt_table)
    unlocked_apts[current_apt] = current_key

    while apt_table:
        for i in range(len(unlocked_apts)):
            current_apt = i
            if unlocked_apts[current_apt] is not None:
                current_key = unlocked_apts[current_apt]
                while apt_table[current_apt]:
                    apt, key = apt_table[current_apt].pop()
                    real_apt = apt - current_key
                    unlocked_apts[real_apt] = key
                del apt_table[current_apt]
    return unlocked_apts[fedor_apt]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
