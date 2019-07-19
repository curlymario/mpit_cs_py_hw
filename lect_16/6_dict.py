# Создадим пустой словарь Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

# Считаем название страны
print('В какой стране вы живёте?')
country = input()

# Проверим, есть ли такая страна в словаре Capitals
if country in Capitals:
    # Если есть — выведем её столицу
    print('Столица вашей страны', Capitals[country])
else:
    # Запросим название столицы и добавим его в словарь
    print('Как назвается столица вашей страны?')
    city = input
    Capitals[country] = city