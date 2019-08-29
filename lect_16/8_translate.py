# ========== Перевод строк ===========

import requests

def import_dict(file_path) -> dict:
    """ Вводим текст из удалённого файла
        Выдаём словарь
    """

    file = requests.get(file_path)
    dictionary = dict()
    for line in file.iter_lines():
        words = line.decode().split("\t-\t")
        dictionary[words[0]] = words[-1]

    return dictionary

if __name__ == "__main__":
