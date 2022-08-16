# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def python_string_slicer(str):
    return  str

def setUpClass(cls):
    cls.service = Service()
    cls.driver = webdriver.Chrome(service=cls.service)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()

@pytest.fixture(scope="function", params=[
    ("https://apps.apple.com/ru/app/лабиринт-ру-книжный-магазин/id1008650482", "Apple AppStore"),
    ("https://play.google.com/store/apps/details?id=ru.labirint.android", "Google Play" ),
    ("https://appgallery.cloud.huawei.com/marketshare/app/C101184737", "Huawei AppGallery")
], ids=["1.Apple AppStore", "2.Google Play", "3.Huawei AppGallery"])
def param_fun(request):
   return request.param

def test_35_click_labirint_club_applications(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   driver = webdriver.Chrome()
   driver.get(result)
   time.sleep(2)
   assert result == driver.current_url