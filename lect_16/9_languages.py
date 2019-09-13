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


def find_countries(requested_language, datalist) -> str:
    """ Получает имя языка (str)
        Ищем совпадения среди значений словаря
        Выдаёт страну(ы) (list)
    """
    result_countries = []
    for country, languages in datalist.items():
        if requested_language in languages:
            result_countries.append(country)
    return result_countries

def input_int(user_input) -> str:
    """ Проверяет, является ли введённый текст числом и преобразует его в int"""
    while True:
        try:
            integer_input = int(user_input)
            break
        except ValueError as e:
            print("You should fisrt enter number, please try again")
            print(e)
    return integer_input

def get_lang_list(datalist):
    """ Пользовательский ввод языков:
        Получает размер списка
        Получает поочерёдно названия языков
        Выводит список стран согласно словарю
    """
    list_len = input_int(input("Пожалуйста, введите число интересующих языков: "))
    for i in range(list_len):
        if i == 0:
            requested_lang = input("Пожалуйста, введите интересующий вас язык\n")
        else:
            requested_lang = input("Пожалуйста, введите следующий язык\n")
        result_countries = find_countries(requested_lang, datalist)
        print(' '.join(result_countries))
    print("Поиск завершён")


if __name__ == "__main__":
    country_lang_list = import_list('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task5/input.txt')
    get_lang_list(country_lang_list)