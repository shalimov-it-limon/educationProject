# страница авторизации
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_class_name = Locators.login_button_class_name
        self.invalidUsername_message_css_selector = Locators.invalidUsername_message_css_selector
        self.invalidPassword_message_css_selector = Locators.invalidPassword_message_css_selector
        self.invalidUsernameAndPassword_css_selector = Locators.invalidUsernameAndPassword_css_selector

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class_name).click()

    def check_invalid_username_message(self):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_2 = self.driver.find_element(By.CSS_SELECTOR, self.invalidUsername_message_css_selector).text
        return msg_2

    def check_invalid_password_message(self):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_3 = self.driver.find_element(By.CSS_SELECTOR, self.invalidPassword_message_css_selector).text
        return msg_3

    def check_invalid_username_and_password_message(self):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        msg_4 = self.driver.find_element(By.CSS_SELECTOR, self.invalidUsernameAndPassword_css_selector).text
        return msg_4
  
