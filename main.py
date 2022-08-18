import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def setUpClass(cls):
    cls.service = Service()
    cls.driver = webdriver.Chrome(service=cls.service)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()

def python_string_slicer(str):
       return 'https://www.labirint.ru'+ str


@pytest.fixture(scope="function", params=[
    ("/now/", "Лабиринт. Сейчас"),
    ("/child-now/", "Детский навигатор" ),
    ("/news/", "Новости Лабиринта"),
    ("/news/books/", "Книжные обзоры"),
    ("/rewievs/", "Рецензии читателей"),
    ("/recomendations/", "Подборки читателей"),
    ("/journals/", "Литературные журналы"),
    ("/awards/", "Литературные премии")
], ids=["1", "2", "3", "4","5","6","7","8"])
def param_fun(request):
   return request.param

def test_python_string_slicer(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   driver = webdriver.Chrome()
   driver.get(result)
   assert result == driver.current_url