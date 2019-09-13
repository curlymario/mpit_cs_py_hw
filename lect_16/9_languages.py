# ========== Страны и языки ===========

import requests

def import_list(file_path) -> dict:
    """ Вводим текст из удалённого файла (ссылка на файл, str)
        Выдаём словарь (dict):
        Ключ: страна (str)
        Значение: языки (str или tuple(str))
    """
    file = requests.get(file_path)
    datalist = dict()
    for line in file.iter_lines(decode_unicode=True):
        dict_entry = line.split(" : ")
        country = dict_entry[0]
        language = {*dict_entry[1].split(" "), }
        datalist[country] = language

    return datalist


def find_countries(language, datalist) -> str:
    """ Получает имя языка (str)
        Ищем совпадения среди значений словаря
        Выдаёт страну(ы) (str)
    """
    pass

def get_lang_list(datalist):
    """ Пользовательский ввод языков:
        Получает размер списка
        Получает поочерёдно названия языков
        Выводит список стран согласно словарю
    """
    pass

if __name__ == "__main__":
    countries_list = import_list('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task5/input.txt')
    print(countries_list)