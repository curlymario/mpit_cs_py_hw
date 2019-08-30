# ========== Перевод строк ===========

import requests

# TODO: Отдельный метод для работы с файлами — найти или написать

def import_dict(file_path) -> dict:
    """ Вводим текст из удалённого файла
        Выдаём словарь
    """

    file = requests.get(file_path)
    dictionary = dict()
    for line in file.iter_lines(decode_unicode=True):
        words = line.split("\t-\t")
        dictionary[words[0]] = words[-1]

    return dictionary

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

def translate(file_path, dictionary):
    """ Вводим текст из удалённого файла
        переводим по словарю
        сохраняем полученный текст в output.txt
    """
    file = requests.get(file_path)
    result = []
    for line in file.iter_lines(decode_unicode=True): # работаю построчно
        line = strip_punct(line.lower()) # убираю пунктуацию и меняю заглавные буквы на прописные
        line_result = []
        for word in line.split():
            if word in dictionary:
                line_result.append(dictionary[word])
            else:
                line_result.append(word)
        result.append(' '.join(line_result)) # соединяю список слов строки в одну строку

    return '\n'.join(result) # соединяю все строки в текст


if __name__ == "__main__":
    en_ru_dict = import_dict('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/en-ru.txt')
    translate_result = translate('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/input.txt', en_ru_dict)
    print(translate_result)