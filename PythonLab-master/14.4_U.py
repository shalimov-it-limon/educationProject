# Функции высшего порялка принимают в качестве аргументов другие функции или возвращают другие функции, как результат.
# Функции, как параметры:
# def my_func(inside_func):
#     ...
#     inside_func()
#     ...
# Как результат:
def a():
    def b():
        pass
    return b

# Функция выполняет принимаемую как аргумент функцию дважды:


def twice_func(inside_func):
    inside_func()
    inside_func()
    inside_func()


def hello():
    print('Hello')


test = twice_func(hello)

# ЗАМЫКАНИЕ - ф-ция, в теле которой присутствуют ссылки на переменные, объявленные вне тела ф-ции и не
# являющиеся ее аргументами. (По принципу NONLOCAL).
# Ф-ция возвращает ф-цию, всегда возвращающую одно число.



def make_adder(x):
    def adder(n):
        return x + n   # ЗАхват переменной "х" из nonlocal области.
    return adder   # Возврат ф-ции в качестве результата.


add_5 = make_adder(6)
print(add_5(10))
print(add_5(100))


# ДЕКОРАТОРЫ подключают любое дополнительное поведение к основной ф-ции, или декорируемой ф-ции,
# которое выполняется ДО, либо ПОСЛЕ, либо ВМЕСТО, оуносвной ф-ции. Исходник не затрагиваем.
# Дополнительным поведением может быть подсчет времени выполнения ф-ции, проверка доп.условий,
# разрешающих проведение ф-ции.


def my_decorator(a_function_to_decorate): # В скобках - декорируемая ф-ция. Декоратор my_decorator принимает
                                          # ф-цию в скобках, как аргумент
    def wrapper():  # Декорируемая ф-ция через замыкание передается в декорированную ф-цию wrapper (стр. 53 - 55)
        result = a_function_to_decorate
        return result
    return wrapper  # Декоррированная ф-ция wrapper добавляет доп. поведение к осн.ф-ции и возвращает сам декоратор
                    # стр 51 - 56.


def my_decorator(a_function_to_decorate):
# Здесь определяется ф-ция - "оберка". Нужна для выполнения каждый раз при вызове оригинальной ф-ции,
# а не только один раз.
    def wrapper():
# Здесь код, который будет выполняться до вызова, потом вызов оригинальной ф-ции,
# потом код после вызова.
      print("Я буду выполнена до основного вызова")

      result = a_function_to_decorate # Обязательно вернуть значение основной ф-ции.

      print("Я буду выполнен после основного вызова!")
      return result
    return wrapper
def my_function():
    print('Я - оборачиваемая ф-ция')
    return 0

print(my_function())

decorated_function = my_decorator(my_function)
print(decorated_function())

import time


def decorator_time(fn):
    def wrapper():
        print(f'Запустилась ф-ция {fn}')
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        print(f'Ф-ция выполнилась. Время: {dt:.10f}')
        return dt # Закодированная ф-ция будет возвращать время работы
    return wrapper


def pow_2():
    return 10000000**2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()

in_build_pow()


# import time
#
#
# def decorator_time(fn):
#     def wrapper():
#         print(f'Запустилась ф-ция {fn}')
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f'Ф-ция выполнилась. Время: {dt:.10f}')
#         return dt # Закодированная ф-ция будет возвращать время работы
#     return wrapper
#
#
# def pow_2():
#     return 10000000**2
#
#
# def in_build_pow():
#     return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#     mean_pow_2 += pow_2()
#     mean_in_build_pow += in_build_pow()
#
# print(f'Ф-ция {pow_2} выполялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}')
# print(f'Ф-ция {in_build_pow} выполялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}')

# pow_2()
#
# in_build_pow()

# СИНТАКСИЧЕСКИЙ САХАР


def my_decorator(fn):
    def wrapper():
        fn()
    return wrapper  # Возвращает задекоррированную ф-цию, заменяющую исходную

# Выводится незадикорированная ф-ция

def my_function():
    pass
print( my_function)

# Выводится задекорированная ф-ция
@my_decorator
def my_function():
    pass
print(my_function)

# Декорирование функции с аргументами:

# def do_it_twice(func):
#     def wrapper():
#         func(arg)
#         func(arg)
#     return wrapper
#
# @do_it_twice
# def say_word(word):
#     print(word)
#
# say_word('Oj!')

# Задекорированная ф-ция wrapper не принимает ни одного аргумента.

def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_it_twice
def say_word(word):
    print(word)

say_word('Oj!')

# Теперь задекорированная ф-ция wrapper принимает аргумент.

# ШАБЛОН ДЕКОРАТОРА


def my_decoorator(fn):
    print('Этот код будет выведен один раз в момент декорирования ф-ции.')
    def wrapper (*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом ф-ции ')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова ф-ции.')
        return result
    return wrapper

# Декоратор, подсчитывающий количество вызовов декорируемой ф-ции. Переменная из nonlocal области.


def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f'Ф-ция {func} была вызвана {count} раз')
    return wrapper


@counter
def say_word(word):
    print(word)

say_word('Hi!')

# Декоратор, который сохраняет результаты выполнения декорируемой ф-ции в словаре. Словарь находится в
# nonlocal области. Ключ - аргумент ф-ции, значение - результат работы ф-ции, например, {n:f(n)}.
# При повторном вызове функции берется значение из словаря.


def cache(func):
    cache_dict = {}
    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f'Добавление результата в кэш: {cache_dict[num]}')
        else:
            print(f'Возвращение результата из кэша: {cache_dict[num]}')
        print(f'Кэш {cache_dict}')
        return cache_dict
    return wrapper


print(cache(1))

