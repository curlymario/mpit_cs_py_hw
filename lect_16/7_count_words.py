# ========== Подсчёт слов ===========
from typing import Dict, Any


def import_text(rel_path) -> str:
    """ Вводим текст из файла (относительный адрес)
        Выдаём строку
        TODO: Сделать отдельную функцию для проверки и получения абсолютного адреса файла
        TODO: Обработать исключения (файл не найден)
    >>> import_text('test_file.txt')
    'text, some text'
    """
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, rel_path)
    file = open(file_path, "rt", encoding="utf-8")
    text = file.read()

    return text


def strip_punct(text):
    """ Компилируем punc = re.compile(string.punctuation)
        Заменяем пунктуацию на пробелы text = puncsub(" ", text)
        Выдаём текст с пробелами без пунктуации
    >>> strip_punct("hi, my name is Maxim! Nice to meet you ;)")
    'hi my name is Maxim Nice to meet you '
    """
    import re
    import string

    punct = re.compile('[%s]' % re.escape(string.punctuation))
    text = punct.sub("", text)

    return text


def count_words(text):
    """ Берёт текст без знаков препинания
        Находим комбинации символов от пробела до пробела
        Если нет в словаре, сохраняет в словарь с ключём из слова и значением 1
        Если есть в словаре, значение += 1
        На выходе словарь
    >>> count_words("hi my name is Maxim it is Nice to meet you ")
    {'hi': 1, 'my': 1, 'name': 1, 'is': 2, 'maxim': 1, 'it': 1, 'nice': 1, 'to': 1, 'meet': 1, 'you': 1}
    """
    text = text.lower()
    table: Dict[str, int] = dict()
    list_of_words = text.split()
    for word in list_of_words:
        if word not in table.keys():
            table[word] = 1
        else:
            table[word] += 1
    return table


def top_10(table):
    """ Берём словарь (создаём его копию? Можно ли избежать изменения оригинального словаря?)
        Пробегаем по всем ключам и находим ключ с максимальным значением
        Делаем так 10 раз, ? каждый раз удаляя предыдущее топ значение ?
    >>> top_10({'hi': 1, 'my': 2, 'name': 3, 'is': 4, 'maxim': 1, 'it': 5, 'nice': 1, 'to': 1, 'meet': 9, 'you': 1, 'me': 1})
    ['meet', 'it', 'is', 'name', 'my', 'hi', 'maxim', 'nice', 'to', 'you']
    """
    list_of_words = []
    table_to_sort = table.copy()
    for _ in range(0, 10):
        word = max(table_to_sort, key=table_to_sort.get)
        table_to_sort.pop(word)
        list_of_words.append(word)
    return list_of_words


if __name__ == "__main__":
    import doctest

    doctest.testmod()