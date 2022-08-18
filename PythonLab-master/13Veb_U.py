# Операторы сравнения
a = 5
b = 7
print(a < b)
print(a > b)
print(a <= b)


def bol_men(a, b):
    if a < b:
        print('Good news')
    elif a > b:
        print('Bad news')
    else:
        print('Strange news')


bol_men(11, 9)
bol_men(5, 9)
bol_men(9, 9)
print('-' * 20)
# Логические операторы


def delit_ne_delit(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print('Good news')
    elif a % 2 == 0 and b % 2 == 1:
        print('Bad news')
    elif a % 2 == 0 or b % 2 == 0:
        print('Vary good news')
    else:
        print('Strange news')


delit_ne_delit(4, 8)
delit_ne_delit(4, 9)
delit_ne_delit(5, 8)
delit_ne_delit(-5, 9)
print('-' * 20)

# Проверка принадлежности

l = [1, 2, 3, 10]
print(*l)
if 2 in l:
    print('I am here!')

# Проверка тождественности
n = [1, 2]
m = [1, 2]
print(n == m)
print(n is m)
print(n is not m)

n = m

print(n == m)
print(n is m)
print(n is not m)
print('-' * 20)
# Тернарный оператор


def ternarniy_operat(x):
    print('Делится на 2 без остатка' if x % 2 == 0 else "Делится на 2 с остатком")


ternarniy_operat(8)


def ostatok_bezostatka(x):
    if x % 3 == 0:
        print(f'{x} делится на 3 без остатка.')
    elif x % 3 != 0:
        print(f'{x} делится на 3 с остатком.')
    else:
        print(f"{x} - страшное простое число!")


ostatok_bezostatka(11e12)


def delu_vse(w, e):
    if e:    # Выполнится, если е != 0, булевое трушное число.
        print(w / e)
        print(round(w / e))
        print(int(w / e))
    else:
        print('И нечего на ноль делить!')


delu_vse(5, 6)
delu_vse(5, 0)
# ВСЕ ПУСТЫЕ ОБЪЕКТЫ - False, имеющие значение - True.

h = []
print(bool(h))
h = {}
print(bool(h))
h = [1]
print(bool(h))
g = {'1': 'a'}
print(type(g))
print(bool(g))


def max_min(a, b):
    print(min(a, b))
    print(max(a, b))


max_min(65, 17)
print('-' * 20)


def max_min(a, b):  # Неправильно! выводит просто значения переменных a b.
    c = min(a, b)
    n = max(a, b)
    return n, c


print(sorted(max_min(106, 25)))
print('-' * 20)


def max_min(a, b):
    min(a, b)
    max(a, b)
    return a and b  # Выполнит второе непустое условие


print(max_min(65, 17))

a = int(input('Число 1: '))
b = int(input('Число 2: '))


def max_min(a, b):
    min(a, b)
    max(a, b)
    return a, b


print(sorted(max_min(max(a, b), min(a, b))))


def max_min(a, b, c, d):
    j = min(a, b, c, d)
    n = max(a, b, c, d)
    return n, j


print(sorted(max_min(106, 25, 1005, 2)))
# print('-' * 20)
#
# # Определить тип треугольника (остроугольный, тупоугольный, прямоугольный по сторонам:
#
a = int(input('Сторона a: '))
b = int(input('Сторона b: '))
c = int(input('Сторона c: '))


def my_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            print('Acute') # Остроугольный
        elif c ** 2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2:
            print('Right')  # Прямоугольный
        elif c ** 2 > a ** 2 + b ** 2 or a ** 2 > c ** 2 + b ** 2 or b ** 2 > a ** 2 + c ** 2:
            print('Obtuse')   # Тупоугольный
        else:
            print('Acute') # Остроугольный
    else:
        print('Impossible')
    p = a + b + c
    return p


print(my_triangle(a, b, c))


# a = int(input('Сторона a: '))
# b = int(input('Сторона b: '))
# c = int(input('Сторона c: '))
# abc = a,  b, c
# g = max(a, b, c)
#
#
# def my_triangle(a, b, c):
#     if (a + b > c) and (b + c > a) and (a + c > b):
#         if a == b == c:
#             print('Acute') # Остроугольный
#         elif g ** 2 == a ** 2 + b ** 2:
#             print('Right')  # Прямоугольный
#         elif c ** 2 > a ** 2 + b ** 2 or a ** 2 > c ** 2 + b ** 2 or b ** 2 > a ** 2 + c ** 2:
#             print('Obtuse')   # Тупоугольный
#         else:
#             print('Acute') # Остроугольный
#     else:
#         print('Impossible')
#
#
# print(my_triangle(a, b, c))
# c ** 2 < a ** 2 + b ** 2 or a ** 2 < c ** 2 + b ** 2 or b ** 2 < a ** 2 + c ** 2:
# Для списка:

l = [1, 2, 'k', [1, 2]]

for var in l:
    print(var)
print(*l)

# for для итерируемых объектов
n = 10
r1 = range(n)
print(r1)
for elem in r1:
    if elem % 2 == 0:
        print('Good elem')
    else:
        print('Bad elem')


print()
print('-' * 20)
n = 20
r1 = range(n)
print(r1)
for elem in r1:
    # c = elem % 2 == 0 STUPID VAR
    if elem % 2 == 0:
        print(f'{elem} - Good elem')
    else:
        print(f'{elem} - Bad elem')


print('-' * 20)
n = 20   # Все элементы
m = 10   # С этого элемента начнем
k = 2    # Шаг
r1 = range(n)
r2 = range(m, n, k)
for elem in r2:
    # c = elem % 2 == 0 STUPID VAR
    if elem % 2 == 0:
        print(f'{elem} - Good elem')
    else:
        print(f'{elem} - Bad elem')

# Цикл while
a = 1

while a < 10:
    a = a * 2  # Каждое новое действие - новая а.
    print(a)
print(a)

# 35-08