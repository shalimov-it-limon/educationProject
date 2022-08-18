# -*- coding: utf-8 -*-
import time

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
    ('//a[@href="/partner/"]', "partner")
], ids=["1.Partnership"])
def param_fun(request):
    return request.param


def test_53_labirint_club_partnership(param_fun):
    (input, expected_output) = param_fun
    driver = webdriver.Chrome()
    driver.get('https://www.labirint.ru/club/')
    result = python_string_slicer(driver, input)
    result.click()
    assert ('https://' + expected_output + '.labirint.ru/login') == driver.current_url
    driver.close()
