import pytest
from selenium import webdriver
import time
import conftest

def test_search_example(driver):
    """ Search some phrase in google and make a screenshot of the page. """
    driver = webdriver.Chrome()  # получение объекта веб-драйвера для нужного браузер
    # Open google search page:
    driver.get('https://google.com')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = driver.find_element_by_name('q')


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = driver.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    driver.save_screenshot('result.png')

    driver.close()


#test_search_example(driver)