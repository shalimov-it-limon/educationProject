# для фикстур
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service


class LabirintTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service()
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_invalid_login_message(self):
        """Ввод неверного телефона/почты/кода при входе в личный кабинет"""
        driver = self.driver
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("12345678910111213")
        message_1 = driver.find_element(By.CSS_SELECTOR,
                                        'form#auth-by-code > div:nth-of-type(3) > span:nth-of-type(3) > small').text
        self.assertEqual(message_1, 'Введенного кода не существует')

    def test_02_valid_login_email(self):
        """Ввод корректного адреса электронной почты при входе в личный кабинет"""
        driver = self.driver
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("arvalan85@mail.ru")
        self.assertNotEqual(homepage.check_discount_code("80C6-442B-82CC"), "")

    def test_03_logout(self):
        """выход из личного кабинета"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_logout_button()

    def test_04_valid_login_code(self):
        """Ввод корректного кода скидки при входе в личный кабинет"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("B74F-4675-94C8")
        self.assertNotEqual(homepage.check_login_successful(), "")

    def test_05_search_execute(self):
        # Поиск на сайте
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        self.assertNotEqual(homepage.click_search_field(), "")

    def test_06_click_labirint_logo(self):
        # Возвращение на главную страницу сайта по нажатию на логотип Лабиринт
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_labirint_logo()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/')

    def test_07_click_messages_button(self):
        # Просмотр сообщений
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_messages_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/')

    def test_08_click_personal_cabinet_button(self):
        # Переход в личный кабинет
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_personal_cabinet_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/')

    def test_09_click_defferet_button(self):
        # Переход в раздел "Отложено"
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_defferet_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/putorder/')

    def test_10_click_cart_button_empty(self):
        # Переход в пустую корзину
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cart/')
        self.assertEqual(homepage.check_empty_cart(), "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?")

    def test_11_click_cart_menu_labirint_now_button(self):
        # Переход в раздел "Лабиринт сейчас" из контекстого меню корзины
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_now()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/now/')

    def test_12_click_cart_menu_main_books_button(self):
        # Переход в раздел "Главные книги" из контекстого меню корзины
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_best()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/best/')

    def test_13_click_cart_menu_create_order(self):
        # Оформление заказа без входа в корзину
        # Дляначала нужно выйти из текущего пользователя
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_logout_button()
        # После этого нужно авторизоваться под пользователем, у которого непустая корзина
        time.sleep(2)
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("arvalan85@mail.ru")
        self.assertNotEqual(homepage.check_discount_code("80C6-442B-82CC"), "")
        # Оформляем заказ по кнопке из контекстного меню корзины
        homepage.click_cart_menu_create_order()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cart/')
        self.assertNotEqual(homepage.check_empty_cart(), "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?")


    def test_14_click_cart_button_not_empty(self):
        # Переход в  непустую корзину
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cart/')
        self.assertNotEqual(homepage.check_empty_cart(), "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?")

    def test_15_click_users_agreement(self):
        #Пользовательское соглашение
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_user_agreement_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/agreement/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()
