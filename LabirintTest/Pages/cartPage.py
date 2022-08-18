# страница корзины
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.locators import Locators
from useful_methods import check_exists_by_xpath


class CartPage:

    def __init__(self, driver):
        self.driver = driver

        self.clear_cart_xpath = Locators.cart_clear_cart_xpath
        self.restore_cart_xpath = Locators.cart_restore_xpath
        self.cart_deffered_xpath = Locators.cart_deffered_xpath
        self.cart_mycart_xpath = Locators.cart_mycart_xpath
        self.cart_deffered_goods_xpath = Locators.cart_deffered_goods_xpath
        self.cart_mycart_goods_xpath = Locators.cart_mycart_goods_xpath
        self.cart_coupon_xpath = Locators.cart_coupon_xpath
        self.cart_coupon_input_xpath = Locators.cart_coupon_input_xpath
        self.cart_coupon_apply_button_xpath = Locators.cart_coupon_apply_button_xpath

    def click_clear_cart(self):
        # Нажимаем на "Очистить корзину"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.clear_cart_xpath)))
        element.click()

    def click_restore_cart(self):
        # Нажимаем на "Восстановить удалённое"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.restore_cart_xpath)))
        element.click()

    def click_cart_deffered(self):
        # Нажимаем на вкладку "Отложенные" на стране корзины
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_deffered_xpath)))
        element.click()

    def check_deffered_goods(self):
        # Проверяем наличие надписи "ОТЛОЖЕННЫЕ ТОВАРЫ" на странице корзины
        return check_exists_by_xpath(self.driver, self.cart_deffered_goods_xpath)

    def click_cart_mycart(self):
        # Нажимаем на вкладку "Моя корзина" на странице корзины
        if not check_exists_by_xpath(self.driver, self.cart_mycart_goods_xpath):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.cart_mycart_xpath())))
            element.click()

    def check_mycart_goods(self):
        # Проверяем наличие надписи "ОТЛОЖЕННЫЕ ТОВАРЫ" на странице корзины
        return check_exists_by_xpath(self.driver, self.cart_mycart_goods_xpath)

    def click_cart_coupon_button(self, coupon):
        # Нажимаем на "Сертификаты и купоны"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_coupon_xpath)))
        element.click()
        input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_coupon_input_xpath)))
        input.send_keys(coupon)
        self.driver.find_element(By.XPATH, self.cart_coupon_apply_button_xpath).click()
