def linear_solve(a,b):
    return b / a


print(linear_solve(5, 25))


def linear_solve(a,b):
    if a:
        return b / a
    else:
        return "Нет корней"


print(linear_solve(6, 4))

def linear_solve(a,b):
    if a:
        return b / a
    elif not a and not b:
        return "Бесконечное количество корней"
    else:
        return "Нет корней"


print(linear_solve(5, 0))

# a*x ** 2 + b*x + c = 0 - Общий вид уравнения
# D = b ** 2 - Дискриминант
# Если D < 0, то уравнениям не имеет вещественных корней.
# Если D = 0, то уравнениям имеет один корень - x = -b/(2*a).
# Если D > 0, то уравнениям имеет 2 вещественных корня.
# x1 = (- b - D**0.5) / (2*a)
# x1 = (- b + D**0.5) / (2*a)
# D**0.5 - = извлечение квадратного корня.


def D(a, b, c):
    return b**2 - 4*a*c


def quadratic_solve(a, b, c):
    def D(a, b, c):
        return b ** 2 - 4 * a * c
    if D(a, b, c) < 0:
        return 'Нет вещественных корней.'
    elif D(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (- b - D(a, b, c) **0.5) / (2*a), (- b + D**0.5) / (2*a)


print(quadratic_solve(25, 2, 56))

# При вводе аргументов с консоли:
# Разбить строку из ввода и преобразовать к float.
# Ввод строки 1 0 -1.
# l = list(map(float, input().split()))
# Вывод [1.0, 0.0, -1.0]
# [1.0.-1] - пример.

# input()
# l = list(map(float, input().split()))
# def D(a, b, c):
#     return b**2 - 4*a*c
#
#
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return 'Нет вещественных корней.'
#     elif D(a, b, c) == 0:
#         return -b/(2*a)
#     else:
#         return (- b - D(a, b, c) **0.5) / (2*a), (- b + D**0.5) / (2*a)
#
#
# print(quadratic_solve(25, 2, 56))

iter_obg = iter('Hello!')
print(next(iter_obg))
print(next(iter_obg))
print(next(iter_obg))
print(next(iter_obg))
print(next(iter_obg))
print(next(iter_obg))

# декоратор проверки авторизации пользователя из встроенных средств Django.
# функция, которая должна извлекать из базы данных какую-то информацию.
yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
    print("some data from database")

from_db()

# функцию-декоратор, которая проверяет доступ к функции по username пользователя.
# Все username пользователей хранятся в глобальной области видимости в списке USERS.
# При согласии пользователя на авторизацию ему предлагается ввести username, который также
# хранится в глобальной области видимости. Функция должна использовать два декоратора:
# один для проверки авторизации вообще (реализован выше), второй — для проверки доступа.

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
                print("Доступ пользователю", username, "запрещен")

    return wrapper


@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()