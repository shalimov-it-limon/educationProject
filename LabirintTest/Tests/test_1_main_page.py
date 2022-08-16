from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service


class MainPageTest(unittest.TestCase):

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
        """ Поиск на сайте"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        self.assertNotEqual(homepage.click_search_field(), "")

    def test_06_click_labirint_logo(self):
        """Возвращение на главную страницу сайта по нажатию на логотип Лабиринт"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_labirint_logo()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/')

    def test_07_click_messages_button(self):
        """Просмотр сообщений"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_messages_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/')

    def test_08_click_personal_cabinet_button(self):
        """Переход в личный кабинет"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_personal_cabinet_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/')

    def test_09_click_defferet_button(self):
        """Переход в раздел "Отложено"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_defferet_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cabinet/putorder/')

    def test_10_click_cart_button_empty(self):
        """Переход в пустую корзину"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cart/')
        self.assertEqual(homepage.check_empty_cart(), "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?")

    def test_11_click_cart_menu_labirint_now_button(self):
        """Переход в раздел "Лабиринт сейчас" из контекстого меню корзины"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_now()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/now/')

    def test_12_click_cart_menu_main_books_button(self):
        """Переход в раздел "Главные книги" из контекстого меню корзины"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_best()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/best/')

    def test_13_click_cart_menu_create_order(self):
        """Оформление заказа без входа в корзину"""
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
        """Переход в  непустую корзину"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/cart/')
        self.assertNotEqual(homepage.check_empty_cart(), "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?")

    def test_15_click_users_agreement(self):
        """Пользовательское соглашение"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_user_agreement_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/agreement/')

    def test_16_click_mainmenu_books_button(self):
        """Нажатие на кнопку "Книги" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_books_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/books/')

    def test_17_click_book_genre(self):
        """Выбор книг определённого жанра"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_genre()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/genres/2994/')

    def test_18_click_mainmenu_best(self):
        """Нажатие на кнопку "Главное <текущий год>" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_best()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/best/')

    def test_19_click_mainmenu_school_button(self):
        """Нажатие на кнопку "Школа" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_school_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/school/')

    def test_20_click_school_english_button(self):
        """Выбор категории "Английский язык" в разделе "Школа" """
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_school_english()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/school/?predmet[]=4#right')

    def test_21_click_mainmenu_games_button(self):
        """Нажатие на кнопку "Игрушки" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_games_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/games/')

    def test_22_click_mainmenu_children_art(self):
        """Выбор раздела "Детское творчество" в категории "Игрушки" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_art()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/genres/3339/')

    def test_23_click_mainmenu_stationery(self):
        """Нажатие на кнопку "Канцтовары" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_stationery_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/office/')

    def test_24_click_mainmenu_stationery_globus(self):
        """Выбор подраздела "Глобусы" в разделе "Канцтовары" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_globus_xpath()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/genres/1500/')

    def test_25_click_mainmenu_submenu_multimedia_button(self):
        """Нажатие на раздел "CD/DVD" подменю "Ещё.." главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cd_dvd_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/multimedia/')

    def test_26_click_mainmenu_submenu_souvenir_button(self):
        """Нажатие на раздел "Сувениры" подменю "Ещё.." главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_souvenir_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/souvenir/')

    def test_27_click_mainmenu_submenu_journals_button(self):
        """Нажатие на раздел "Журналы" подменю "Ещё.." главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_journals_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/journals/')

    def test_28_click_mainmenu_submenu_household_button(self):
        """Нажатие на раздел "Товары для дома" подменю "Ещё.." главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_household_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/household/')

    def test_29_click_mainmenu_club_button(self):
        """Нажатие на кнопку "Клуб" главного меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_club_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/club/')

    def test_51_click_mainmenu_region_button(self):
        """Нажатие на название региона в главном меню"""
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_region_button()
        self.assertEqual(self.driver.current_url, 'https://www.labirint.ru/club/')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()
