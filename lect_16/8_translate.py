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

if __name__ == "__main__":
