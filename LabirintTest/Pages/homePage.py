# основная страница
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
        self.books_button_xpath = Locators.books_button_xpath
        self.books_games_xpath = Locators.books_gameworld_xpath
        self.books_comix_xpath = Locators.books_comix_xpath
        self.school_button = Locators.school_button_xpath
        self.school_predmet_english_xpath = Locators.school_predmet_english_xpath
        self.games_button_xpath = Locators.games_button_xpath
        self.children_art_xpath = Locators.children_art_xpath
        self.diamond_mozaik_xpath = Locators.diamonds_mozaic_xpath
        self.stationery_xpath = Locators.stationery_xpath
        self.globus_xpath = Locators.globus_xpath
        self.mainmenu_submenu_xpath = Locators.mainmenu_submenu_xpath
        self.multimedia_xpath = Locators.multimedia_xpath
        self.souvenir_xpath = Locators.souvenir_xpath
        self.journals_xpath = Locators.journals_xpath
        self.household_xpath = Locators.household_xpath
        self.club_xpath = Locators.club_xpath
        self.region_xpath = Locators.region_xpath
        self.region_input_xpath = Locators.region_input_xpath
        self.map_xpath = Locators.map_xpath
        self.delivery_date_filter_xpath = Locators.delivery_date_filter_xpath
        self.delivery_date_xpath = Locators.delevery_dates_select_all_xpath
        self.delivery_point_caption_xpath = Locators.delivery_point_caption_xpath
        self.delivery_point_ymaps_xpath = Locators.delivery_point_ymaps_xpath
        self.secondary_menu_xpath = Locators.delivery_and_paymen_button_xpath

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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.personal_discount_xpath)))
        return element.text

    def click_logout_button(self):
        # Наводим курсор мыши на кнопку "Мой Лаб"
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
        # Для валидности проверки сначала перейдём на другую страницу, например, поиска
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
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.labirint_logo_xpath)))
        element.click()

    def click_personal_cabinet_button(self):
        # Переход в личный кабинет
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.top_menu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.top_menu_xpath)[1]
        element.click()

    def click_messages_button(self):
        # Нажимаем на кнопку "Сообщения"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.messages_xpath)))
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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_menu_create_order_xpath)))
        element = self.driver.find_elements(By.XPATH, self.cart_menu_create_order_xpath)[1]
        element.click()

    def check_empty_cart(self):
        # Проверка наличия сообщения о пустой корзине
        if check_exists_by_xpath(self.driver, self.empty_cart_xpath):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.empty_cart_xpath)))
            return element.text

    def click_user_agreement_button(self):
        # Нажимаем на пользовательское соглашение
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.users_agreement_xpath)))
        element = self.driver.find_elements(By.XPATH, self.users_agreement_xpath)[1]
        element.click()

    def click_books_button(self):
        # Нажимаем на кнопку "Книги" главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.books_button_xpath)))
        element = self.driver.find_elements(By.XPATH, self.books_button_xpath)[0]
        element.click()

    def click_genre(self):
        # Наводим курсор на кнопку "Книги"
        books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.books_button_xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(books)
        actions.perform()
        # Наводим на категорию "Комиксы,Манга,Артбуки
        comix = self.driver.find_elements(By.XPATH, self.books_comix_xpath)[2]
        actions = ActionChains(self.driver)
        actions.move_to_element(comix)
        actions.perform()
        # Нажимаем на "Артбуки.Игровые миры.Вселенные
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.books_games_xpath)))
        element.click()

    def click_best(self):
        # Нажимаем на кнопку "Главное <текущий год>"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart_menu_best_xpath)))
        element = self.driver.find_elements(By.XPATH, self.cart_menu_best_xpath)[2]
        element.click()

    def click_school_button(self):
        # Нажимаем на кнопку "Книги" главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.school_button)))
        element = self.driver.find_elements(By.XPATH, self.school_button)[0]
        element.click()

    def click_school_english(self):
        # Наводим курсор на "Школа"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.school_button)))
        element = self.driver.find_elements(By.XPATH, self.school_button)[1]
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        # Нажимаем на "Английский язык"
        english = self.driver.find_element(By.XPATH, self.school_predmet_english_xpath)
        english.click()

    def click_games_button(self):
        # Нажимаем на кнопку "Игрушки" главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.games_button_xpath)))
        element = self.driver.find_elements(By.XPATH, self.games_button_xpath)[0]
        element.click()

    def click_children_art(self):
        # Наводим на "Игрушки"
        games = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.games_button_xpath)))
        games = self.driver.find_elements(By.XPATH, self.games_button_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(games)
        actions.perform()
        # Наводим курсор на "Детское творчество"
        children_art = self.driver.find_element(By.XPATH, self.children_art_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(children_art)
        actions.perform()
        # Нажимаем на "Алмазные мозаики
        diamond_mozaik = self.driver.find_element(By.XPATH, self.diamond_mozaik_xpath)
        diamond_mozaik.click()

    def click_stationery_button(self):
        # Нажимаем на кнопку "Канцтовары" главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.stationery_xpath)))
        element = self.driver.find_elements(By.XPATH, self.stationery_xpath)[0]
        element.click()

    def click_globus_xpath(self):
        # Наводим курсор на канцтовары
        games = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.stationery_xpath)))
        games = self.driver.find_elements(By.XPATH, self.stationery_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(games)
        actions.perform()
        # Нажимаем на "Глобусы"
        globus = self.driver.find_element(By.XPATH, self.globus_xpath)
        globus.click()

    def click_cd_dvd_button(self):
        # Наводим курсор на кнопку "Ещё..." главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mainmenu_submenu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.mainmenu_submenu_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        # Нажимаем на CD/DVD
        multimedia = self.driver.find_elements(By.XPATH, self.multimedia_xpath)[-2]
        multimedia.click()

    def click_souvenir_button(self):
        # Наводим курсор на кнопку "Ещё..." главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mainmenu_submenu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.mainmenu_submenu_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        # Нажимаем на "Сувениры"
        souvenir = self.driver.find_elements(By.XPATH, self.souvenir_xpath)[-2]
        souvenir.click()

    def click_journals_button(self):
        # Наводим курсор на кнопку "Ещё..." главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mainmenu_submenu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.mainmenu_submenu_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        # Нажимаем на "Журналы"
        souvenir = self.driver.find_elements(By.XPATH, self.journals_xpath)[-2]
        souvenir.click()

    def click_household_button(self):
        # Наводим курсор на кнопку "Ещё..." главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mainmenu_submenu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.mainmenu_submenu_xpath)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        # Нажимаем на "Товары для дома"
        souvenir = self.driver.find_elements(By.XPATH, self.household_xpath)[-2]
        souvenir.click()

    def click_club_button(self):
        # Нажимаем на кнопку "Клуб" главного меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.club_xpath)))
        element = self.driver.find_elements(By.XPATH, self.club_xpath)[0]
        element.click()

    def change_region_name(self):
        # Нажимаем на кнопку с названием региона в главном меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.region_xpath)))
        element.click()
        # В поле ввода нового наименования региона вводим новое название
        element_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.region_input_xpath)))
        element_input.clear()
        element_input.send_keys("Пермь")
        time.sleep(2)
        element_input.send_keys(Keys.ENTER)
        # Возвращаем новое название региона
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.region_xpath)))
        return element.text

    def change_delivery_params(self):
        # Нажимаем на кнопку, вызывающую карту
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.map_xpath)))
        element = self.driver.find_elements(By.XPATH, self.map_xpath)[0]
        element.click()
        # Переходим на карту
        # Нажимаем на фильтр дат доставки
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.delivery_date_filter_xpath)))
        element.click()
        # В выпадающем списке выбираем первый элемент
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.delivery_date_xpath)))
        element.click()
        # Выбираем первый пункт самовывоза из списка
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.delivery_point_caption_xpath)))
        element = self.driver.find_elements(By.XPATH, self.delivery_point_caption_xpath)[0]
        element.click()
        # Проверяем наличие всплывающего окошка с информацией о пункте самовывоза
        popup_baloon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.delivery_point_ymaps_xpath)))
        return check_exists_by_xpath(self.driver, self.delivery_point_ymaps_xpath)

    def click_delivery_and_payment_button(self):
        # Нажимаем на кнопку "Доставка и оплата" меню
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.secondary_menu_xpath)))
        element = self.driver.find_elements(By.XPATH, self.secondary_menu_xpath)[0]
        element.click()
