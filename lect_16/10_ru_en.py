# ========== Перевод словаря ===========

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
    result_dict = dict()
    for original_word, translation in original_dict.items():
        for translated_word in translation.split(", "):
            if translated_word in result_dict:
                result_dict[translated_word].append(original_word)
                result_dict[translated_word].sort()
            else:
                result_dict[translated_word] = [original_word, ]
    return result_dict

def export_dict(dictionary, target_file):
    """ Получает словарь, сортирует и сохраняет в файл """
    dict_lines = ["\t-\t".join((key, ", ".join(value))) for key, value in dictionary.items()]
    dict_lines.sort()
    file = open(target_file, "w+", encoding="utf8")
    for line in dict_lines:
        file.write(line + "\n")
    file.close()
    return dict_lines

if __name__ == "__main__":
    en_ru = import_dict('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task6/en-ru.txt')
    ru_en = reverse_dict(en_ru)
    export_dict(ru_en, "ru-en.txt")