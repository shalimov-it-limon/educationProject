# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def python_string_slicer(driver, str):
    element = driver.find_elements(By.XPATH, str)[0]
    return element


def setUpClass(cls):
    cls.service = Service()
    cls.driver = webdriver.Chrome(service=cls.service)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()


@pytest.fixture(scope="function", params=[
    ('//a[@href="/best/"]', "/best/"),
    ('//a[@href="/top/certificates/"]', "/top/certificates/"),
    ('//a[@href="/exclusive/"]', "/top/exclusive/"),
    ('//a[@href="/top/skoro-v-prodazhe/"]', "/top/skoro-v-prodazhe/")
], ids=["1.Labirint best", "2.Certificates", "3.Exclusives", "4.Book for preorder"])
def param_fun(request):
    return request.param


def test_46_49_labirint_club_labirint_only(param_fun):
    (input, expected_output) = param_fun
    driver = webdriver.Chrome()
    driver.get('https://www.labirint.ru/club/')
    result = python_string_slicer(driver, input)
    result.click()
    assert ('https://www.labirint.ru' + expected_output) == driver.current_url
    driver.close()
