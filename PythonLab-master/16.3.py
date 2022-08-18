user_peter = {
    "name": "Peter",
    "email": "peterrobertson@mail.com",
    "created_at": "2019-05-05",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
}

user_julia = {
    "name": "Julia Donaldson",
    "email": "juliadonaldson@mail.com",
    "created_at": "2019-06-13",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Magic Brush"],
}

product_eggs = {
    "name": "Egg",
    "category": "food",
    "is_available": False,
    "quantity_in_stock": 0,
    "vendor": "Dark Knight LTD",
    "manager": "William The Conqueror",
}

def is_product_available(product):
    return True if product["quantity_in_stock"] > 0 else False


class User:
    pass

peter = User()  # вызвали класс, как функцию, с помощью скобок
peter.name = "Peter Robertson"  # Здесь .name — это атрибут экземпляра нашего класса. Атрибуты позволяют хранить
                                # произвольные данные в привязке к конкретному экземпляру

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)
# В этом смысле классы и экземпляры классов работают так же,
# как и модули: они создают пространство имён, в котором доступны
# различные сущности. Как мы видим, после создания экземпляра мы смогли каждому экземпляру
# задать произвольный атрибут и положить в него уникальное значение.

peter.email = "peterrobertson@mail.com"
print(peter.email)
# print('\n')
# print(julia.email)

# Создание произвольного атрибута у одного экземпляра не привело ни к каким изменениям
# у второго, что логично. Можно сравнить классы с формой и инструкцией для выпекания пирогов,
# а экземпляры — с конкретными испечёнными пирогами.
# Если вы откусили кусок от одного, это никак не повлияет на остальные.

# Мы можем задавать атрибуты, которые будут доступны из любого объекта, причём без дополнительных действий.
# Для этого их надо объявлять прямо внутри класса:


class User:

    number_of_fingers = 5
    number_of_eyes = 2


lancelot = User()


print(lancelot.number_of_fingers)