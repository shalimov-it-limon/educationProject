# Метод — это всего лишь функция, реализованная внутри класса,
# и первым аргументом принимающая self.

class Product:    # Здесь и __init__, и is_available — это методы.
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


eggs = Product("eggs", "food", 5)
print(eggs.is_available())
print(eggs.quantity_in_stock)
print(eggs.category)

# Для вызова метода, как и для вызова функции, используются круглые скобки.
# Разница между методом и функцией только в том, что метод вызывается от конкретного
# объекта и реализован внутри класса,
# а функция работает сама по себе.

#  обрабатывать некоторые события из уже известных нам логов событий. Создадим класс с конструктором:


class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

# уже распарсили наши логи и получили список словарей вроде такого:

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

# для каждого события в списке создадим соответствующий ему объект с помощью конструктор

for event in events:
    event_obj = Event(timestamp=event.get("timestamp"), # get возвращает значение словаря по ключу в скобках
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)  # чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:

# мы могли бы задать нашему классу метод,
# который позволяет инициализировать наш объект напрямую.
#  поправим объявление нашего класса и зададим для каждой переменной её значение
# по умолчанию, чтобы мы могли инициализировать объект без заполнения.
# Это делается с помощью указания значений по умолчанию сразу после названия аргумента:


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

# теперь добавим метод. Не забываем, что метод принимает на вход self первым аргументом.

    def init_from_dict(self, event_dict):   # Метод идет с отступом и должен быть объявлен внутри класса.
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

# скрыли реализацию логики от пользователя — то есть нам уже неважно,
# как это работает, мы знаем, что можем подать на вход словарь с нужными ключами


for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

# классы — это связка между определенной структурой данных,
# хранящихся в атрибутах, и логикой, которая непосредственно относится к ним.