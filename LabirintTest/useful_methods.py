from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def check_exists_by_xpath(driver, xpath):
    """Метод проверяющий наличие элемента на странице"""
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True