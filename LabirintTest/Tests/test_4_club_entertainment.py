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
    ("/littest/", "Литтесты"),
    ("/contests/", "Конкурсы" ),
    ("/fun/", "Дома с детьми")
], ids=["1.Littests", "2.Contests", "3.Labirint for fun"])
def param_fun(request):
   return request.param

def test_33_click_labirint_club_entertainment(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   driver = webdriver.Chrome()
   driver.get(result)
   time.sleep(2)
   assert result == driver.current_url