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
    ('//a[@href="/now/"]', "/now/"),
    ('//a[@href="/child-now/"]', "/child-now/"),
    ('//a[@href="/news/"]', "/news/"),
    ('//a[@href="/news/books/"]', "/news/books/"),
    ('//a[@href="/reviews/"]', "/reviews/"),
    ('//a[@href="/recommendations/"]', "/recommendations/"),
    ('//a[@href="/journals/"]', "/journals/"),
    ('//a[@href="/award/"]', "/award/")
], ids=["1.Labirint now", "2.Labirint for children now", "3.Labirint news", "4.Book news", "5.Book rewievs",
        "6.Recomendations", "7.Literature magazines", "8.Literature awards"])
def param_fun(request):
    return request.param


def test_38_45_labirint_club_journal(param_fun):
    (input, expected_output) = param_fun
    driver = webdriver.Chrome()
    driver.get('https://www.labirint.ru/club/')
    result = python_string_slicer(driver, input)
    result.click()
    assert ('https://www.labirint.ru' + expected_output) == driver.current_url
    driver.close()
