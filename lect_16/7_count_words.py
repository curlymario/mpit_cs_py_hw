# ========== Подсчёт слов =========== 

def import_text(rel_path) -> str:
    """ Вводим текст из файла (относительный адрес)
        Выдаём строку
        TODO: Сделать отдельную функцию для проверки и получения абсолютного адреса файла
        TODO: Обработать исключения (файл не найден)

    >>> import_text("test_file.txt")
    'text,\nsome text'
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
    #>>> strip_punct("hi, my name is Maxim! Nice to meet you ;)")
    #"hi my name is Maxim Nice to meet you "
    """  
    import re
    import string

    punct = re.compile(string.punctuation)
    text = punct.sub("", text)

    return text

def count_words(text):
    """ Берёт текст без знаков препинания
        Находим комбинации символов от пробела до пробела
        Если нет в словаре, сохраняет в словарь с ключём из слова и значением 1
        Если есть в словаре, значение += 1
        На выходе словарь
    # >>> count_words("hi my name is Maxim it is Nice to meet you ")
    # {'hi': 1, 'my': 1, 'name': 1, 'is': 2, 'Maxim': 1, 'it': 1, Nice': 1, 'to': 1, 'meet': 1, 'you': 1}
    """
    pass

def top_10(dict):
    """ Берём словарь (создаём его копию? Можно ли избежать изменения оригинального словаря?)
        Пробегаем по всем ключам и находим ключ с максимальным значением
        Делаем так 10 раз, ? каждый раз удаляя предыдущее топ значение ?
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()