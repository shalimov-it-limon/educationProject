# для фикстур
# python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path C:\Users\Татьяна\PycharmProjects\Projects_3\chromedriver.exe Tests\login.py
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


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
        homepage.click_personal_cabinet_button("12345678910111213")
        message_1 = driver.find_element(By.CSS_SELECTOR,
                                        'form#auth-by-code > div:nth-of-type(3) > span:nth-of-type(3) > small').text
        self.assertEqual(message_1, 'Введенного кода не существует')

    def test_02_valid_login_email(self):
        """Ввод корректного адреса электронной почты при входе в личный кабинет"""
        driver = self.driver
        driver.get('https://www.labirint.ru/cabinet')
        homepage = HomePage(driver)
        homepage.click_personal_cabinet_button("arvalan85@mail.ru")
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
        homepage.click_personal_cabinet_button("B74F-4675-94C8")
        self.assertNotEqual(homepage.check_login_successful(), "")

    '''
    def test_02_invalid_password_message(self):
        """Ввод неверного пароля"""
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username('login')
        login.enter_password('password')
        login.click_login()
        login.check_invalid_password_message()
        time.sleep(3)
        message_2 = driver.find_element(By.CSS_SELECTOR, '#content-box > div > div').text
        self.assertEqual(message_2, 'Логин или пароль введен неправильно')

    def test_03_invalid_username_and_password_message(self):
        """Ввод неверных логина и пароля"""
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username('con.t20152@yandex.ru')
        login.enter_password('58890v18555')
        login.click_login()
        login.check_invalid_password_message()
        message_3 = driver.find_element(By.CSS_SELECTOR, '#content-box > div > div').text
        self.assertEqual(message_3, 'Логин или пароль введен неправильно')

    def test_04_login_valid(self):
        """Ввод верных логина и пароля"""
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username('con.t2012@yandex.ru')
        login.enter_password('58890v18')
        login.click_login()
        message_4 = driver.find_element(By.CSS_SELECTOR, '#content-box > div > h2').text
        self.assertEqual(message_4, 'Вы успешно авторизированы!')

    def test_05_click_my_tabs(self):
        """Проверка кликабельности кнопки 'Мои закладки'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_tabs()

        message_5 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_5, 'Мои закладки')

    def test_06_click_my_orders(self):
        """Проверка кликабельности кнопки 'Мои заказы'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_orders()

        message_6 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_6, 'Мои заказы')

    def test_07_click_my_profile(self):
        """Проверка кликабельности кнопки 'Мой профиль'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_my_profile()

        message_7 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_7, 'Мой профиль')

    def test_08_contact_info_message(self):
        """Наличие контактной информации в моем профиле"""
        driver = self.driver

        message_8 = driver.find_element(By.CSS_SELECTOR,
                                        '#register > tbody:nth-child(1) > tr:nth-child(1) > td > h2').text
        self.assertEqual(message_8, 'Контактная информация')

    def test_09_delivery_info_message(self):
        """Наличие информации о доставке в моем профиле"""
        driver = self.driver

        message_9 = driver.find_element(By.CSS_SELECTOR,
                                        '#register > tbody:nth-child(3) > tr:nth-child(1) > td > h2').text
        self.assertEqual(message_9, 'Информация о доставке')

    def test_10_other_info_message(self):
        """Наличие дополнительной информации в моем профиле"""
        driver = self.driver

        message_10 = driver.find_element(By.CSS_SELECTOR,
                                         '#register > tbody:nth-child(3) > tr:nth-child(5) > td > h2').text
        self.assertEqual(message_10, 'Дополнительная информация')

    def test_11_click_change_password(self):
        """Проверка кликабельности кнопки 'Сменить пароль'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_change_password()

        message_11 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_11, 'Сменить пароль')

    def test_12_new_password_value(self):
        """Наличие поля 'Новый пароль' в графе сменить пароль"""
        driver = self.driver

        message_12 = driver.find_element(By.CSS_SELECTOR, '#register > tbody > tr:nth-child(1) > td:nth-child(1)').text
        self.assertEqual(message_12, 'Новый пароль:*')

    def test_13_confirmation_new_password_value(self):
        """Наличие поля 'Подтверждение пароля' в графе сменить пароль"""
        driver = self.driver

        message_13 = driver.find_element(By.CSS_SELECTOR, '#register > tbody > tr:nth-child(2) > td:nth-child(1)').text
        self.assertEqual(message_13, 'Подтвержение пароля:*')

    def test_14_old_password_value(self):
        """Наличие поля 'Старый пароль' в графе сменить пароль"""
        driver = self.driver

        message_14 = driver.find_element(By.CSS_SELECTOR, '#register > tbody > tr:nth-child(3) > td:nth-child(1)').text
        self.assertEqual(message_14, 'Старый пароль:*')

    def test_15_click_basket(self):
        """Проверка кликабельности кнопки 'В корзине'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_basket()

        message_15 = driver.find_element(By.CSS_SELECTOR, '#basket > div.basket-h > a').text
        self.assertEqual(message_15, 'В корзине')

    def test_16_click_catalog_products(self):
        """Проверка выпадающего списка при нажатие на каталог товаров"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_catalog_products()

        product = [
            'Страйкбольное оружие\nПистолеты\nАккумуляторы и ЗУ\nСтрайкбольная пиротехника\nАксессуары\nАмуниция\nЗапч'
            'асти\nМагазины\nОчки, маски, шлема\nПрицелы, коллиматоры, крепления\nРасходники\nСувениры, сертификаты']

        message_16 = [element.text for element in driver.find_elements(By.XPATH, '//*[@id="menu"]/div/div/div')]
        self.assertEqual(product, message_16)

    def test_17_click_airsoft_guns(self):
        """Проверка кликабельности кнопки 'Страйкбольное оружие' в каталоге товаров"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_airsoft_guns()

        message_17 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_17, 'Оружие для страйкбола')

    def test_18_lens_products_and_imgs(self):
        """Сравнения количества товаров и картинок к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_all_guns()  # категорию "все" открывает с большим трудом (сайт виснет, тест может упасть)

        products = driver.find_elements(By.CLASS_NAME, 'product')
        imgs = driver.find_elements(By.CLASS_NAME, 'product_img')

        self.assertEqual(len(products), len(imgs))

    def test_19_lens_product_and_name(self):
        """Сравнения количества товаров и названия к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        names = driver.find_elements(By.CLASS_NAME, 'name')

        self.assertEqual(len(products), len(names))

    def test_20_lens_product_and_brands(self):
        """Сравнения количества товаров и наличие бренда к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        brands = driver.find_elements(By.CLASS_NAME, 'brand_name')

        self.assertEqual(len(products), len(brands))

    def test_21_lens_product_and_prices(self):
        """Сравнения количества товаров и цены к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        prices = driver.find_elements(By.CLASS_NAME, 'product-price-wrapper')

        self.assertEqual(len(products), len(prices))

    def test_22_lens_product_and_button_pay(self):
        """Сравнения количества товаров и кнопки 'Купить' к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        button_pay = driver.find_elements(By.CLASS_NAME, 'buy')

        self.assertEqual(len(products), len(button_pay))

    def test_23_lens_product_and_button_detailed(self):
        """Сравнения количества товаров и кнопки 'Подробнее' к ним (категория 'Страйкбольное оружие')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        button_detailed = driver.find_elements(By.CLASS_NAME, 'detailed')

        self.assertEqual(len(products), len(button_detailed))

    def test_24_check_buys(self):
        """Добавление товара в корзину (Страйкбольная винтовка (ARES) Amoeba STRIKER S1 Black AS01-BK).
        Наличие кнопки 'Оформить заказ' в ней"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_button_buy_vint1()
        time.sleep(5)
        homepage.click_basket()

        message_24 = driver.find_element(By.ID, 'order_button').is_displayed()
        self.assertEqual(message_24, True)

    def test_25_more_buys(self):
        """Наличие кнопки '+' для увеличения количества товара в корзине"""
        driver = self.driver

        message_25 = driver.find_element(By.XPATH,
                                         '//*[@id="basket_detailed"]/div[2]/table/tbody[2]/tr/td[2]/div[2]/span/a[2]').is_displayed()
        self.assertEqual(message_25, True)

    def test_26_delete_buys(self):
        """Наличие кнопки 'х' для удаления товара из корзины"""
        driver = self.driver

        message_26 = driver.find_element(By.XPATH,
                                         '//*[@id="basket_detailed"]/div[2]/table/tbody[2]/tr/td[6]/button').is_displayed()
        self.assertEqual(message_26, True)

    def test_27_promo(self):
        """Наличия поля для ввода промокода (корзина)"""
        driver = self.driver

        message_27 = driver.find_element(By.ID, 'coupon_code_text').is_displayed()
        self.assertEqual(message_27, True)

    def test_28_click_pyrotechnics(self):
        """Проверка кликабельности кнопки 'Страйкбольная пиротехника' в каталоге товаров"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_catalog_products()
        homepage.click_pyrotechnics()

        message_28 = driver.find_element(By.XPATH, '//*[@id="content-box"]/h1').text
        self.assertEqual(message_28, 'Страйкбольная пиротехника')

    def test_29_lens_products_and_imgs(self):
        """Сравнения количества товаров и картинок к ним (категория 'Страйкбольная пиротехника')"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_all_guns_2()  # категорию "все" открывает с большим трудом (сайт виснет)

        products = driver.find_elements(By.CLASS_NAME, 'product')
        imgs = driver.find_elements(By.CLASS_NAME, 'product_img')

        self.assertEqual(len(products), len(imgs))

    def test_30_lens_product_and_name(self):
        """Сравнения количества товаров и названия к ним (категория 'Страйкбольная пиротехника')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        names = driver.find_elements(By.CLASS_NAME, 'name')

        self.assertEqual(len(products), len(names))

    def test_31_lens_product_and_prices(self):
        """Сравнения количества товаров и цен к ним (категория 'Страйкбольная пиротехника')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        prices = driver.find_elements(By.CLASS_NAME, 'product-price-wrapper')

        self.assertEqual(len(products), len(prices))

    def test_32_lens_product_and_button_pay(self):
        """Сравнения количества товаров и кнопки 'Купить' к ним (категория 'Страйкбольная пиротехника')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        button_pay = driver.find_elements(By.CLASS_NAME, 'buy')

        self.assertEqual(len(products), len(button_pay))

    def test_33_lens_product_and_button_detailed(self):
        """Сравнения количества товаров и кнопки 'Подробнее' к ним (категория 'Страйкбольная пиротехника')"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        button_detailed = driver.find_elements(By.CLASS_NAME, 'detailed')

        self.assertEqual(len(products), len(button_detailed))

    def test_34_click_new_products(self):
        """Проверка кликабельности кнопки 'Новинки'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_new_products()

        message_34 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_34, 'Новинки')

    def test_35_click_sale(self):
        """Проверка кликабельности кнопки 'Распродажа'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_sale()

        message_35 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_35, 'Распродажа')

    def test_36_click_discounts_and_bonuses(self):
        """Проверка кликабельности кнопки 'Скидки и бонусы'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_discounts_and_bonuses()

        message_36 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_36, 'Скидки и бонусы')

    def test_37_click_payment_and_delivery(self):
        """Проверка кликабельности кнопки 'Оплата и доставка'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_payment_and_delivery()

        message_37 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_37, 'Оплата и доставка')

    def test_38_click_hurry_up(self):
        """Проверка кликабельности кнопки 'Успей купить'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_hurry_up()

        message_38 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_38, 'Успей купить')

    def test_39_lens_products_count_and_timer(self):
        """Наличие таймера на всех продуктах в категории 'Успей купить'"""
        driver = self.driver

        products = driver.find_elements(By.CLASS_NAME, 'product')
        button_detailed = driver.find_elements(By.CLASS_NAME, 'countdownHolder')

        self.assertEqual(len(products), len(button_detailed))

    def test_40_click_contacts(self):
        """Проверка кликабельности кнопки 'Контакты'"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_contacts()

        message_34 = driver.find_element(By.CSS_SELECTOR, '#content-box > h1').text
        self.assertEqual(message_34, 'Контакты')

    def test_41_click_link_vk(self):
        """Проверка корректности кнопки с ссылкой на группу в ВК"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_vk()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(2)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_42_click_link_facebook(self):
        """Проверка корректности кнопки с ссылкой на группу в фейсбук"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_facebook()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(3)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_43_click_link_twitter(self):
        """Проверка корректности кнопки с ссылкой на группу в твиттер"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_twitter()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(4)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_44_click_link_instagram(self):
        """Проверка корректности кнопки с ссылкой на группу в инстаграм"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_instagram()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(5)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_45_click_link_youtube(self):
        """Проверка корректности кнопки с ссылкой на группу в ютуб"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_link_youtube()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(6)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)
        # тест падает, так как ссылка в коде не соответсвует реальной ссылке
        # не критично, канал на ютубе открывается нужный

        driver.close()

    def test_46_click_link_telegram_bot(self):
        """Проверка корректности кнопки с ссылкой на бота в телеграм"""
        driver = self.driver
        driver.get('https://airsoftsports.ru')

        homepage = HomePage(driver)
        homepage.click_link_telegram_bot()

        link_from_shop_page = driver.find_element(
            By.CSS_SELECTOR, '#content-left > div.social-main > a:nth-child(7)').get_attribute('href')
        driver.switch_to.window(driver.window_handles[2])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_47_click_email_us(self):
        """Появления формы для отправки отзыва после нажатия на кнопку 'НАПИСАТЬ НАМ' в подвале сайта"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_email_us()
        time.sleep(5)
        message_47 = driver.find_element(By.XPATH, '/html/body/div[15]').is_displayed()
        self.assertEqual(message_47, True)

        homepage.click_close_the_form()

    def test_48_lens_articles_and_news(self):
        """Проверка, что каждая статья несет текстовую информацию"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_articles()

        articles = driver.find_elements(By.CLASS_NAME, 'news-text')
        news = driver.find_elements(By.LINK_TEXT, 'Читать полностью')

        self.assertEqual(len(articles), len(news))

    def test_49_presence_brands(self):
        """Проверка, что на главной странице сайта представлены бренды, с которыми работает компания"""
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_top_logo()

        message_49 = driver.find_element(By.CLASS_NAME, 'brands-main-block').is_displayed()
        self.assertEqual(message_49, True)

    def test_50_presence_find(self):
        """Проверка налия строки поиска на сайте"""
        driver = self.driver

        message_50 = driver.find_element(By.ID, 'find').is_displayed()
        self.assertEqual(message_50, True)'''

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()
