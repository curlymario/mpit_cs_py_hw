# ========== Перевод строк ===========

import requests

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

def reverse_dict(original_dict):
    """ Получает словарь, выдаёт обратный словарь """
    pass

def export_dict(dictionary):
    """ Получает словарь, сортирует и сохраняет в файл """
    pass