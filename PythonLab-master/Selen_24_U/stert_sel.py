from selenium import webdriver
import time
import pytest
# driver = webdriver.Firefox()

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Firefox('/usr/local/bin/')


def test_example(driver):
    driver.get('https://www.google.com/')
    time.sleep(10)
    search_input = driver.find_element_by_name('q')

    search_input.clear()
    search_input.send_keys('И тут я что-то печатаю')

    time.sleep(10)

    search_button = driver.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)

    driver.save_screenshot('resault.png')
    # driver.close()



# driver.close()