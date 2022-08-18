from datetime import datetime
from decorator import do_twice

def sum(a, b):
    return a + b


print(sum(5, 9))


def say_hello(name):
    return f"Hello, {name}!"


def be_awesome(name):
    return f"Yo, {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))
print(greet_bob(be_awesome))


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    first_child()
    second_child()
    first_child()


print(parent())


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


print(parent(4))
first = parent(1)
second = parent(2)
print(first())
print(second())
first = parent(3)
print(first())


# def custom_func(num):
# 	print("Calling function") # Смотри в НИЧТО. Эта функция с побочным эффектом,
#                               # в ней не задан явно тип возвращаемого значения, поэтому вернется none.

def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

#Эту функцию мы будем декорировать
def my_first_decorator():
	print("Это мой первый декоратор!")

my_decor = my_decorator(my_first_decorator)

print(my_decor())
# print(my_decorator()) # Ошибка. Нет функции, как аргумента функции.

def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Нерабочее время, выходим
    return wrapper

def writing_tests():
    print("Я пишу тесты на python!")

writing_tests = working_hours(writing_tests)

print(writing_tests())


def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")


print(my_first_decorator())

# @do_twice
# def test_twice():
#     print("Это вызов функции test_twice!")