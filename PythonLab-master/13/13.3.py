# Блок-схема — это способ графического представления алгоритма,
# в котором шаги изображаются в виде блоков различной формы, соединенных между собой стрелками.
rain = True # Код основной проги. Первый уровень вложенности - не содержит отступов.
if rain:
    print("Бери зонт!")
else:
    print("Не бери зонт.")
a = 7
b = 9 + a
print('a = F(', b, ')')
print('-' * 20)

mx = 0
s = 0
x = int(input())
if x < 0:
    s = 0
b = 7
b /= b
if x > mx:
    mx = x
print(s)
print(mx)
print('-' * 50)

is_rainy = True  # дождь будет
heavy_rain = False  # не сильный дождь
# Вложенные условные операторы
if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")
print(bool(0))  # False
print(bool(1))  # True

print(bool("")) # False
print(bool("1"))  # True

print(bool([])) # False
print(bool([1]))  # True
# Плохо. Ошибка.
# if zero != 0:
#    print(10 / zero)
# else:
#    print("Делить на ноль нельзя")

# Хорошо
zero = 0
if zero:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")
print('-' * 50)

# Плохо
if password == "":
   print("Вы забыли ввести пароль")
else:
   ...

# Очень плохо
if len(password) == 0:
   print("Вы забыли ввести пароль")
else:
   ...

# Хорошо
if not password:
   print("Вы забыли ввести пароль")
else: