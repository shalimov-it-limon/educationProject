# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def python_string_slicer(str):
    return 'https://www.labirint.ru' + str

def setUpClass(cls):
    cls.service = Service()
    cls.driver = webdriver.Chrome(service=cls.service)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()

@pytest.fixture(scope="function", params=[
    ("/now/", "Лабиринт. Сейчас"),
    ("/child-now/", "Детский навигатор" ),
    ("/news/", "Новости Лабиринта"),
    ("/news/books/", "Книжные обзоры"),
    ("/rewievs/", "Рецензии читателей"),
    ("/recomendations/", "Подборки читателей"),
    ("/journals/", "Литературные журналы"),
    ("/awards/", "Литературные премии")
], ids=["1.Labirint now", "2.Labirint for children now", "3.Labirint news", "4.Book news","5.Book rewievs","6.Recomendations","7.Literature magazines","8.Literature awards"])
def param_fun(request):
   return request.param

def test_30_click_labirint_club_journal(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   driver = webdriver.Chrome()
   driver.get(result)
   time.sleep(2)
   assert result == driver.current_url