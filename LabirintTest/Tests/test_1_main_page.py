from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

from Pages.homePage import HomePage
from Pages.cartPage import CartPage
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
        self.assertEqual('Введенного кода не существует', message_1)

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
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_logout_button()

    def test_04_valid_login_code(self):
        """Ввод корректного кода скидки при входе в личный кабинет"""
        driver = self.driver
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("B74F-4675-94C8")
        self.assertNotEqual(homepage.check_login_successful(), "")

    def test_05_search_execute(self):
        """ Поиск на сайте"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        self.assertNotEqual(homepage.click_search_field(), "")

    def test_06_click_labirint_logo(self):
        """Возвращение на главную страницу сайта по нажатию на логотип Лабиринт"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_labirint_logo()
        self.assertEqual('https://www.labirint.ru/', self.driver.current_url)

    def test_07_click_messages_button(self):
        """Просмотр сообщений"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_messages_button()
        self.assertEqual('https://www.labirint.ru/cabinet/', self.driver.current_url)

    def test_08_click_personal_cabinet_button(self):
        """Переход в личный кабинет"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_personal_cabinet_button()
        self.assertEqual('https://www.labirint.ru/cabinet/', self.driver.current_url)

    def test_09_click_defferet_button(self):
        """Переход в раздел "Отложено"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_defferet_button()
        self.assertEqual('https://www.labirint.ru/cabinet/putorder/', self.driver.current_url)

    def test_10_click_cart_button_empty(self):
        """Переход в пустую корзину"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        self.assertEqual('https://www.labirint.ru/cart/', self.driver.current_url)
        self.assertEqual("ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?", homepage.check_empty_cart())

    def test_11_click_cart_menu_labirint_now_button(self):
        """Переход в раздел "Лабиринт сейчас" из контекстного меню корзины"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_now()
        self.assertEqual('https://www.labirint.ru/now/', self.driver.current_url)

    def test_12_click_cart_menu_main_books_button(self):
        """Переход в раздел "Главные книги" из контекстного меню корзины"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_menu_best()
        self.assertEqual('https://www.labirint.ru/best/', self.driver.current_url)

    def test_13_click_cart_menu_create_order(self):
        """Оформление заказа без входа в корзину"""
        # Для начала нужно выйти из текущего пользователя
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_logout_button()
        # После этого нужно авторизоваться под пользователем, у которого непустая корзина
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_login_operations("arvalan85@mail.ru")
        self.assertNotEqual(homepage.check_discount_code("80C6-442B-82CC"), "")
        # Оформляем заказ по кнопке из контекстного меню корзины
        homepage.click_cart_menu_create_order()
        self.assertEqual('https://www.labirint.ru/cart/', self.driver.current_url)
        self.assertNotEqual("ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?", homepage.check_empty_cart(), )

    def test_14_click_cart_button_not_empty(self):
        """Переход в  непустую корзину"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cart_button()
        self.assertEqual('https://www.labirint.ru/cart/', self.driver.current_url)
        self.assertNotEqual("ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?", homepage.check_empty_cart())

    def test_15_click_users_agreement(self):
        """Пользовательское соглашение"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_user_agreement_button()
        self.assertEqual('https://www.labirint.ru/agreement/', self.driver.current_url)

    def test_16_click_mainmenu_books_button(self):
        """Нажатие на кнопку "Книги" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_books_button()
        self.assertEqual('https://www.labirint.ru/books/', self.driver.current_url)

    def test_17_click_book_genre(self):
        """Выбор книг определённого жанра"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_genre()
        self.assertEqual('https://www.labirint.ru/genres/2994/', self.driver.current_url)

    def test_18_click_mainmenu_best(self):
        """Нажатие на кнопку "Главное <текущий год>" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_best()
        self.assertEqual('https://www.labirint.ru/best/', self.driver.current_url)

    def test_19_click_mainmenu_school_button(self):
        """Нажатие на кнопку "Школа" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_school_button()
        self.assertEqual('https://www.labirint.ru/school/', self.driver.current_url)

    def test_20_click_school_english_button(self):
        """Выбор категории "Английский язык" в разделе "Школа" """
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_school_english()
        self.assertEqual('https://www.labirint.ru/school/?predmet[]=4#right', self.driver.current_url)

    def test_21_click_mainmenu_games_button(self):
        """Нажатие на кнопку "Игрушки" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_games_button()
        self.assertEqual('https://www.labirint.ru/games/', self.driver.current_url)

    def test_22_click_mainmenu_children_art(self):
        """Выбор раздела "Детское творчество" в категории "Игрушки" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_art()
        self.assertEqual('https://www.labirint.ru/genres/3339/', self.driver.current_url)

    def test_23_click_mainmenu_stationery(self):
        """Нажатие на кнопку "Канцтовары" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_stationery_button()
        self.assertEqual('https://www.labirint.ru/office/', self.driver.current_url)

    def test_24_click_mainmenu_stationery_globus(self):
        """Выбор подраздела "Глобусы" в разделе "Канцтовары" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_globus_xpath()
        self.assertEqual('https://www.labirint.ru/genres/1500/', self.driver.current_url)

    def test_25_click_mainmenu_submenu_multimedia_button(self):
        """Нажатие на раздел "CD/DVD" подменю "Ещё.." главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_cd_dvd_button()
        self.assertEqual('https://www.labirint.ru/multimedia/', self.driver.current_url)

    def test_26_click_mainmenu_submenu_souvenir_button(self):
        """Нажатие на раздел "Сувениры" подменю "Ещё.." главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_souvenir_button()
        self.assertEqual('https://www.labirint.ru/souvenir/', self.driver.current_url)

    def test_27_click_mainmenu_submenu_journals_button(self):
        """Нажатие на раздел "Журналы" подменю "Ещё.." главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_journals_button()
        self.assertEqual('https://www.labirint.ru/journals/', self.driver.current_url)

    def test_28_click_mainmenu_submenu_household_button(self):
        """Нажатие на раздел "Товары для дома" подменю "Ещё.." главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_household_button()
        self.assertEqual('https://www.labirint.ru/household/', self.driver.current_url)

    def test_29_click_mainmenu_club_button(self):
        """Нажатие на кнопку "Клуб" главного меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_club_button()
        self.assertEqual('https://www.labirint.ru/club/', self.driver.current_url)

    def test_30_click_mainmenu_region_button(self):
        """Нажатие на название региона в главном меню"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.change_region_name()
        self.assertEqual("Пермь", homepage.change_region_name())

    def test_31_change_delivery_parameters(self):
        """Изменений параметров доставки"""
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        self.assertEqual(True, homepage.change_delivery_params())

    def test_32_click_delivery_and_payment_button(self):
        """Нажатие на кнопку "Доставка и оплата" """
        driver = self.driver
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_delivery_and_payment_button()
        self.assertEqual('https://www.labirint.ru/maps/', self.driver.current_url)

    def test_33_click_clear_cart_button(self):
        """Нажатие на кнопку очистки корзины"""
        driver = self.driver
        homepage = HomePage(driver)
        cartpage = CartPage(driver)
        # Переходим в корзину
        driver.get('https://www.labirint.ru/cart/')
        # Нажимаем на "Очистить корзину"
        cartpage.click_clear_cart()
        self.assertEqual("ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?", homepage.check_empty_cart(), )

    def test_34_click_restore_cart_button(self):
        """Нажатие на кнопку очистки корзины"""
        driver = self.driver
        homepage = HomePage(driver)
        cartpage = CartPage(driver)
        # Переходим в корзину
        driver.get('https://www.labirint.ru/cart/')
        cartpage.click_restore_cart()
        self.assertNotEqual("ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?", homepage.check_empty_cart(), )

    def test_35_click_deffered_card_button(self):
        """Нажатие на вкладку "Отложенные" на странице корзины"""
        driver = self.driver
        cartpage = CartPage(driver)
        # Переходим в корзину
        driver.get('https://www.labirint.ru/cart/')
        cartpage.click_cart_deffered()
        # Проверяем наличие на странице обозначения "ОТЛОЖЕННЫЕ ТОВАРЫ"
        assert (cartpage.check_deffered_goods())

    def test_36_click_mycart_card_button(self):
        """Нажатие на вкладку "Моя корзина" на странице корзины"""
        # Для тестирования функционала корзины нужно зайти в учётку с непустой корзиной
        driver = self.driver
        cartpage = CartPage(driver)
        # Переходим в корзину
        driver.get('https://www.labirint.ru/cart/')
        cartpage.click_cart_mycart()
        # Проверяем наличие на странице обозначения "ВАШ ЗАКАЗ"
        assert (cartpage.check_mycart_goods())

    def test_37_click_cart_coupon_button(self):
        """Применение купона к заказу"""
        # Для тестирования функционала корзины нужно зайти в учётку с непустой корзиной
        driver = self.driver
        cartpage = CartPage(driver)
        # Переходим в корзину
        driver.get('https://www.labirint.ru/cart/')
        # Нажимаем на "Сертификаты и купоны"
        cartpage.click_cart_coupon_button("N39F82W6RZ")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()
