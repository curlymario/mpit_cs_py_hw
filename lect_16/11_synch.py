# ========== Синхронизация словарей ===========

def import_dict(file_path) -> dict:
    """ Вводим текст из удалённого файла
        Выдаём словарь, где:
        key -> str
        value -> list
    """
    pass

def update_dict(target, source) -> dict:
    """ Берём два словаря
        Дополняем значения target ключами из source
        и ключи target значениями из source,
        если таковых в нём нет
        Возвращаем обновлённый словарь target
    """
    pass

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
    en_ru = import_dict('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/en-ru.txt')
    ru_en = import_dict('http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/ru-en.txt')
    en_ru_updated = update_dict(en_ru, ru_en)
    ru_en_updated = update_dict(ru_en, en_ru)
    export_dict(en_ru, "en-ru.txt")
    export_dict(ru_en, "ru-en.txt")


