from selenium import webdriver
import pytest
# import time
# import other
driver = webdriver.Firefox()


# def test_search_example(driver):
# driver = webdriver.Firefox()
driver.get('https://www.google.com/')
search_input = driver.find_element_by_name('q')
search_input.clear()
search_input.send_keys('И тут я что-то печатаю')
search_button = driver.find_element_by_name('btnK')
search_button.submit()
driver.save_screenshot('resault.png')


# driver.close()

