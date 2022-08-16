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
    ("/patner/", "Партнерство")
], ids=["1.Partnership"])
def param_fun(request):
   return request.param

def test_34_click_labirint_club_parntnership(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   driver = webdriver.Chrome()
   driver.get(result)
   time.sleep(2)
   assert result == driver.current_url