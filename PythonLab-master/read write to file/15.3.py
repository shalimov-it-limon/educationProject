# JSON — это такой способ хранения текстовых данных, когда данные хранятся в виде
# пар ключ-значение, и он похож на словарь в Python.
#  JSON — это не словарь и у него есть свои особенности.
#  Поэтому для комфортной работы с JSON существует модуль json.

# Импортируем модуль JSON.
# Открываем файл на чтение(не забываем прописать encoding, так
# как в файле имеются русские буквы).
# Присваиваем переменной результат работы метода load() из модуля JSON.

import json

with open('../json_example.json', encoding="utf8") as f:
    templates = json.load(f)
print(templates)
print(type(templates))
# Результат — это словарь.
# Существует метод loads(), который считывает не файл, а строку.

import json

with open('../json_example.json', encoding='utf8') as f:
    strfile = f.read()
    templates = json.loads(strfile)

print(templates)
print(type(templates))

# метод read() читает весь файл в строчку, так что в переменной strfile теперь просто строка.
# Эту строку тоже можно преобразовать в объект словаря, и за это как раз отвечает метод loads().
# существуют два варианта преобразования словаря в Python в JSON — метод dump() и dumps().
# Первый записывает файл, а второй — строку.
import json

template = {
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'isAlive': True,
    'age': 32,
    'address': {
        'streetAddress': 'Нейбута 32',
        'city': 'Владивосток',
        'state': '',
        'postalcode': ''
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '123-333-4455'
        },
        {
            'type': 'office',
            'number': '123 111-4567'
        }
    ],
    'children': [],
    'spouse': None
}

with open('../to_json_example.json', 'w', encoding='utf8') as f:
    json.dump(template, f, ensure_ascii=False, indent=4)

with open('../to_json_example.json', encoding='utf8') as f:
    print(f.read())