from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()
# driver = webdriver.Firefox('D:\\Общие документы\\AnnCherdan\\Python\\geckodriver.exe')
# driver.get("http://www.python.org")

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox()
   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('shalimov@it-limon.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('Bn3s6wp9')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()


   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"