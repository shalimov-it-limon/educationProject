# # print("Перед исключением")
# # I = 1 / 0 # Здесь что-то не так….
# # print("После исключения")
#
# print("Перед исключением")
# # теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# c = a / b # здесь может возникнуть исключение деления на ноль
# print(c) # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:
# print(e) # Выводим информацию об ошибке
# print("После исключения")
#
# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится, если всё хорошо прошло в блоке try*
# finally:
#     *Код, который выполнится в любом случае*
# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")
# print('-' * 50)
#
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")

try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

try:
    i = int(input('Введите число:\t'))
except ValueError as e:
    print('Вы ввели неправильное число')
else:
    print(f'Вы ввели {i}')
finally:
    print('Выход из программы')