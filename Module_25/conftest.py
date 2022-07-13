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


