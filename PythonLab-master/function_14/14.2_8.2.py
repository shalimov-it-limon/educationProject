def sump_ab(a, b):
    result = a + b
    return result


c = sump_ab(5, 6)
print(c)


def my_c():    # Вызываем функцию sump_ab(a, b) в другом месте и другой функции.
    print(c)


my_c()
print('-' * 20)
# Просчитываем площадь круга S = pi * r**2.
print('My GOOD Var')
# pi = 3, 14 ТАК НЕ РАБОТАЕТ, потому что видит строку, а не переменную. Всегда "."!!!
pi = 3.14    # Глобальная переменная


def area_circle(r):    # аргумент - радиус окружности.
    s = pi * (r ** 2)  # s = pi * int(r ** 2)
    return s


print(area_circle(3.5))

print('Skill GOOD Var')

PI = 3.14


def area_circle(r):
    return PI * (r**2)


print(area_circle(10))
print('My GOOD Var, но делать так не надо!')
# pi = 3, 14 ТАК НЕ РАБОТАЕТ, потому что видит строку, а не переменную. Всегда "."!!!

pi = 3.14    # Глобальная переменная


def area_circle(r):    # аргумент - радиус окружности.
    # print(pi)    # Здесь пи не печатается, потому что имя «пи» используется ПЕРЕД глобальным объявлением.
    global pi    # Объявляем глобальность пи
    # print('OLD pi: ', pi)     # Здесь пи печатается, потому что имя «пи» используется ПОСЛЕ глобальным объявлением.
    pi = 3.1415926   # Здесь изменяется ГЛОБАЛЬНАЯ переменная пи.
    # print('NEW pi: ', pi)
    s = pi * (r ** 2)  # s = pi * int(r ** 2)
    return s

print('OLD pi: ', pi)
print(area_circle(3.5))
print('NEW pi: ', pi)