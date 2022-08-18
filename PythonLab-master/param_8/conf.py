import pytest
import requests
import json


@pytest.fixture(scope='function', params=[
    ('abcdefg', 'abcdefg?'),
    ('abc', 'abc!'),
    ('abcde', 'abcde.')
])
def param_test(request):
    return request.param


def my_decorator(func):
    def wrapper():
        print('Начало выполнения функции.')
        func()
        print('Конец выполнения функции.')
    return wrapper()


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@pytest.fixture
def some_data():
    return 42


@pytest.fixture
def key_param(func):
    response = requests.get(url='https://petfriends.skillfactory.ru/login',
                       data={'email': 'anchetest@mail.ru', 'password': 'ljkmvtyf'})







@pytest.fixture
def pet_key():
    res = requests.post(url='https://petfriends.skillfactory.ru/api/create_pet_simple')