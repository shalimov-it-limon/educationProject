import pytest
from conf import my_decorator
from conf import do_twice
from conf import some_data
from conf import key_param

# # def my_decorator(func):
# #     def wrapper():
# #         print('Начало выполнения функции.')
# #         func()
# #         print('Конец выполнения функции.')
# #     return wrapper()
#
#
# def my_first_decorator():
#     print('Мой первый декоратор.')
#
# my_first_decorator = my_decorator(my_first_decorator)


@my_decorator
def my_first_decorator():
    print('Мой первый декоратор.')


@do_twice
def test_twice_without_params():
    print('Этот вызов без параметоров.')


# @do_twice
# def test_twice(str):
#     print('Этот вызов возвращает строку {0}'.format(str))
#
#
# @do_twice
# def test_twice_2_params(str):
#     print('Этот вызов бултыхает две строки - {0} и {1}.'.format(str1, srt2))

def test_some_data(some_data):
    assert some_data == 42





