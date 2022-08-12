# страница пользовательского профиля
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from Locators.locators import Locators
from useful_methods import check_exists_by_xpath


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        '''
        self.welcome_css_selector = Locators.welcome_css_selector
        self.click_my_tabs_css_selector = Locators.click_my_tabs_css_selector
        self.my_tabs_link_text = Locators.my_tabs_link_text
        self.my_orders_link_text = Locators.my_orders_link_text
        self.my_profile_link_text = Locators.my_profile_link_text
        self.contact_info_link_text = Locators.contact_link_text
        self.delivery_info_link_text = Locators.delivery_info_link_text
        self.other_info_link_text = Locators.other_info_link_text
        self.change_password_link_text = Locators.change_password_link_text
        self.new_password_class_name = Locators.new_password_class_name
        self.confirmation_new_password_class_name = Locators.confirmation_new_password_class_name
        self.old_password_class_name = Locators.old_password_class_name
        self.exit_link_text = Locators.exit_link_text
        self.basket_id = Locators.basket_id
        self.catalog_products_class_name = Locators.catalog_products_class_name
        self.new_products_xpath = Locators.new_products_xpath
        self.sale_xpath = Locators.sale_xpath
        self.discounts_and_bonuses_xpath = Locators.discounts_and_bonuses_xpath
        self.payment_and_delivery_xpath = Locators.payment_and_delivery_xpath
        self.hurry_up_xpath = Locators.hurry_up_xpath
        self.contacts_xpath = Locators.contacts_xpath
        self.airsoft_guns_xpath = Locators.airsoft_guns_xpath
        self.all_guns_xpath = Locators.all_guns_xpath
        self.pyrotechnics_xpath = Locators.pyrotechnics_xpath
        self.all_guns_xpath_2 = Locators.all_guns_xpath_2
        self.link_vk_xpath = Locators.link_vk_xpath
        self.link_facebook_xpath = Locators.link_facebook_xpath
        self.link_twitter_xpath = Locators.link_twitter_xpath
        self.link_instagram_xpath = Locators.link_instagram_xpath
        self.link_youtube_xpath = Locators.link_youtube_xpath
        self.link_telegram_bot_xpath = Locators.link_telegram_bot_xpath
        self.email_us_css_selector = Locators.email_us_css_selector
        self.close_the_form_css_selector = Locators.close_the_form_css_selector
        self.articles_xpath = Locators.articles_xpath
        self.top_logo_css_selector = Locators.top_logo_css_selector
        self.button_buy_vint1_xpath = Locators.button_buy_vint1_xpath
        
        '''

        ###############################################ТУТ НАЧИНАЮТСЯ ЛОКАТОРЫ ЛАБИРИНТА######################################
        self.my_lab_xpath = Locators.my_lab_button_xpath
        self.main_menu_xpath = Locators.main_menu_xpath
        self.cookie_policy_button_xpath = Locators.cookie_policy_botton_xpath
        self.login_xpath = Locators.login_input_xpath
        self.authorize_xpath = Locators.authorization_button_xpath
        self.discount_code_xpath = Locators.discount_code_xpath
        self.authorization_email_sent_button_xpath = Locators.authorization_email_sent_button_xpath
        self.succesfull_login_popup_xpath = Locators.succesfull_login_popup_xpath
        self.search_field_xpath = Locators.search_field_xpath
        self.logout_link_xpath = Locators.logout_link_xpath
        self.personal_discount_xpath = Locators.discount_code_div_xpath
        self.search_button_xpath = Locators.search_button_xpath
        self.search_result_xpath = Locators.search_result_xpath
        self.labirint_logo_xpath = Locators.labirint_logo_xpath
        self.messages_xpath = Locators.messages_xpath
        self.top_menu_xpath = Locators.top_menu_xpath
        self.cart_menu_now_xpath = Locators.labirint_now_xpath
        self.cart_menu_best_xpath = Locators.labirint_best_xpath
        self.cart_menu_create_order_xpath = Locators.cart_create_order_xpath
        self.empty_cart_xpath = Locators.empty_cart_xpath
        self.users_agreement_xpath = Locators.users_agreement_xpath

    def click_login_operations(self, login):
        # Вводим телефон/почту/код скидки
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_elements(By.XPATH, '//input')[5])
        actions.double_click()
        actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(login)
        actions.perform()

        # Нажимаем на "Войти"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.authorize_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.double_click()
        actions.perform()
        time.sleep(2)

    def check_discount_code(self, code):
        # Вводим код скидки в соответствующее поле
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.discount_code_xpath)))
        self.driver.find_elements(By.XPATH, self.discount_code_xpath)[1].send_keys(code)

        # Нажимаем на "Войти"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.authorization_email_sent_button_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.double_click()
        actions.perform()

        # Проверяем, что на главной форме появилось всплывающее сообщение с информацией о скидке
        if check_exists_by_xpath(self.driver, self.succesfull_login_popup_xpath):
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.succesfull_login_popup_xpath)))
        else:
            if check_exists_by_xpath(self.driver, self.personal_discount_xpath):
                element = self.driver.find_elements(By.XPATH, self.personal_discount_xpath)[0]
        return element.text

    def check_login_successful(self):
        # Получаем код скидки из главной страницы сайта
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.personal_discount_xpath)))
        return element.text

    def click_logout_button(self):
        # Наводим курсор мыши на кнопку "Мой Лаб"
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.main_menu_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_elements(By.XPATH, self.main_menu_xpath)[3])
        actions.perform()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.logout_link_xpath)))
        element.click()

    def click_search_field(self):
        # В строку поиска вводим то, что хотим найти
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search_field_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("А.С.Пушкин")
        actions.perform()
        # Нажимаем на кнопку поиска
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        # Смотрим результаты поиска
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search_result_xpath)))
        return element.text

    def click_labirint_logo(self):
        # Нажатие на логотип "Лабиринт" для возвращения на главную страницу
        # Для валидности проверки сначала перейдём на другую страницу, напрмер, поиска
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search_field_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("А.С.Пушкин")
        actions.perform()
        # Нажимаем на кнопку поиска
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        # Теперь прожимаем логотип лабиринта
        time.sleep(2)
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.labirint_logo_xpath)))
        element.click()

    def click_personal_cabinet_button(self):
        # Переход в личный кабинет
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        time.sleep(2)
        element = self.driver.find_elements(By.XPATH, self.top_menu_xpath)[1]
        element.click()

    def click_messages_button(self):
        # Нажимаем на кнопку "Сообщения"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.messages_xpath)))
        time.sleep(2)
        element.click()

    def click_defferet_button(self):
        # Нажимаем на "Отложено"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.top_menu_xpath)[2]
        element.click()

    def click_cart_button(self):
        # Нажимаем на корзину
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.top_menu_xpath)[3]
        element.click()

    def click_cart_menu_now(self):
        # Наводим курсор на корзину
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_elements(By.XPATH, self.top_menu_xpath)[3])
        actions.perform()
        # Нажимаем на "Лабиринт сейчас" контекстного меню корзины
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_menu_now_xpath)))
        element = self.driver.find_elements(By.XPATH, self.cart_menu_now_xpath)[0]
        element.click()

    def click_cart_menu_best(self):
        # Наводим курсор на корзину
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_elements(By.XPATH, self.top_menu_xpath)[3])
        actions.perform()
        # Нажимаем на "Главные книги" контекстного меню корзины
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_menu_best_xpath)))
        element = self.driver.find_elements(By.XPATH, self.cart_menu_best_xpath)[0]
        element.click()

    def click_cart_menu_create_order(self):
        # Наводим курсор на корзину
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_elements(By.XPATH, self.top_menu_xpath)[3])
        actions.perform()
        # Нажимаем на "Главные книги" контекстного меню корзины
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_menu_create_order_xpath)))
        element = self.driver.find_elements(By.XPATH, self.cart_menu_create_order_xpath)[1]
        element.click()

    def check_empty_cart(self):
        # Проверка наличия сообщения о пустой корзине
        if check_exists_by_xpath(self.driver, self.empty_cart_xpath):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.empty_cart_xpath)))
            return (element.text)

    def click_user_agreement_button(self):
        # Нажимаем на пользовательнское соглашение
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.users_agreement_xpath)))
        element = self.driver.find_elements(By.XPATH, self.users_agreement_xpath)[1]
        element.click()
