import webbrowser

from base_page import BasePage
from locators import AuthLocators
from selenium import webdriver

import time,os

class AuthPage(BasePage):
    driver = webdriver.Chrome

    def start(self):
        driver = webdriver.Chrome
        driver.current_url
        super().__init__(driver)
        url = os.getenv("LOGIN_URL") or "http://petfriends1.herokuapp.com/login"
        self.driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(3)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()




