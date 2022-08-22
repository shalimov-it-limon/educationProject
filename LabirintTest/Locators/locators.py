class Locators:
    # login page objects (в лабиринте не используются)
    username_textbox_name = 'login'
    password_textbox_name = 'password'
    login_button_class_name = 'auth_button'
    invalidUsername_message_css_selector = '#content-box > div > div'
    invalidPassword_message_css_selector = '#content-box > div > div'
    invalidUsernameAndPassword_css_selector = '#content-box > div > div'

    # home page objects
    # Кнопка "Мой Лаб" главного меню
    my_lab_button_xpath = '//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]/span[1]/span[1]/span[1]'
    # Кнопка "Сообщения" главного меню
    messages_button_xpath = '//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/span[1]/span[1]'
    # Главное меню
    main_menu_xpath = '//ul[@class = "b-header-b-personal-e-list ul-justify"]/li'
    # Этот локатор не работает :-Р
    cookie_policy_botton_xpath = '//button[@class="cookie-policy__button js-cookie-policy-agree"]'
    # Поле ввода почты/телефона/кода скидки
    login_input_xpath = '//input'
    # Кнопка "Войти" на форме авторизации
    authorization_button_xpath = '//*[@id="g-recap-0-btn"]'
    # Поле ввода кода скидки (появляется после ввода адреса почты)
    discount_code_xpath = "//input[@name='code']"
    # Кнопка "Войти" на форме ввода почты
    authorization_email_sent_button_xpath = '//*[@id="auth-email-sent"]/input[5]'
    # Всплывающее сообщение с информацией о скидке
    succesfull_login_popup_xpath = "//span[@class='popup-nib-tip']"
    # Кнопка "Выход" всплывающего меню "Мой Лаб"
    logout_link_xpath = '//a[@class="user-top-menu-link user-top-menu-link_logout"]'
    # Код скидки из главной страницы сайта
    discount_code_div_xpath = "//div[@class='max-width discount-code']"
    # Строка поиска
    search_field_xpath = '//*[@id="search-field"]'
    # Кнопочка с лупой в строке поиска
    search_button_xpath = "//button[@class='b-header-b-search-e-btn']"
    # Результаты поиска (Товары <какое-то число>)
    search_result_xpath = '//*[@id="stab-slider-frame"]/ul[1]/li[1]'
    # Логотип лабиринта
    labirint_logo_xpath = '//a[@class="b-header-b-logo-e-logo-wrap"]'
    # Кнопка "Сообщения" главного меню
    messages_xpath = '//span[@class="b-header-b-personal-e-icon-wrapper"]'
    # Главное меню
    top_menu_xpath = "//span[@class='b-header-b-personal-e-wrapper-m-closed']"
    # Ссылка для пеоехода на страницу "Лабиринт сейчас"
    labirint_now_xpath = '//a[@href="/now"]'
    # Ссылка для пеоехода на страницу "Главные книги/Главное 2022/ещё какие-то варианты.."
    labirint_best_xpath = '//a[@href="/best/"]'
    # Кнопка "Оформить заказ"
    cart_create_order_xpath = '//a[@title="Оформить заказ"]'
    # Сообщение "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?"
    empty_cart_xpath = '//*[@id="basket-step1-default"]/div[1]/span'
    # Ссылка на пользовательское соглашение
    users_agreement_xpath = "//a[@href='/agreement/']"
    # Ссылка на раздел "Книги" главного меню
    books_button_xpath = "//a[@href='/books/']"
    # Список элементов выпадающего меню раздела "Книги"
    books_comix_xpath = "//span[@class='b-menu-list-title b-menu-list-title-first']"
    # Ссылка раздела сайта "Артбуки. Игровые миры. Вселенные"
    books_gameworld_xpath = "//a[@href='/genres/2994']"
    # Ссылка на радел "Школа" главного меню
    school_button_xpath = "//a[@href='/school/']"
    # Ссылка раздела сайта "Английский язык"
    school_predmet_english_xpath = '//a[@href="/school/?predmet[]=4#right"]'
    # Ссылка на раздел "Игрушки" главного меню
    games_button_xpath = '//a[@href="/games/"]'
    # Ссылка на подраздел "Детское творчество" раздела "Игрушки"
    children_art_xpath = '//*[@id="header-toys"]/div[1]/ul[1]/li[3]/span[1]'
    # Ссылка раздела сайта "Алмазные мозаики"
    diamonds_mozaic_xpath = '//a[@href="/genres/3339"]'
    # Ссылка на раздел "Канцтовары" главного меню
    stationery_xpath = "//a[@href='/office/']"
    # Ссылка на подраздел "Глобусы" раздела "Канцтовары"
    globus_xpath = "//a[@href = '/genres/1500']"
    # кнопка "Ещё..." главного меню
    mainmenu_submenu_xpath = '//span[@class="b-header-b-menu-e-text"]'
    # Раздел "Мультимедиа" (CD/DVD) подменю "Ещё..."
    multimedia_xpath = "//a[@href='/multimedia/']"
    # Раздел "Сувениры" подменю "Ещё..."
    souvenir_xpath = "//a[@href='/souvenir/']"
    # Раздел "Журналы" подменю "Ещё..."
    journals_xpath = "//a[@href='/journals/']"
    # Раздел "Товары для дома" подменю "Ещё..."
    household_xpath = "//a[@href='/household/']"
    # Ссылка на раздел "Клуб" главного меню сайта
    club_xpath = "//a[@href='/club/']"
    # Кнопка с названием региона в главном меню
    region_xpath = '//span[@class="region-location-icon-txt "]'
    # Поле ввода нового наименования региона
    region_input_xpath = '//input[@id="region-post"]'
    # Ссыла на карту
    map_xpath = '//a[@href="/maps/"]'
    # Фильтр дат доставки на карте
    delivery_date_filter_xpath = '//*[@id="js-delivery-date-filter"]'
    # Вариант "все дни" из перечня возможных дат доставки
    delevery_dates_select_all_xpath = '//*[@id="delivery-dates-popup-window"]/div[2]/div[1]'
    # Список пунктов самовывоза
    delivery_point_caption_xpath = '//div[@class = "delivery-point__caption"]'
    # Всплывающее окошко с информацией о пункте самовывоза
    delivery_point_ymaps_xpath = '//*[@id="delivery-point-map"]/ymaps/ymaps/ymaps/ymaps[7]/ymaps/ymaps/ymaps/ymaps[1]/ymaps[2]'
    # Меню с кнопками "Доставка и оплата", "Сертификаты", "Рейтинги", "Новинки", "Скидки" и т.д.
    delivery_and_paymen_button_xpath = '//a[@class ="b-header-b-sec-menu-e-link"]'

    #cart page objects
    # Ссылка "Очистить корзину"
    cart_clear_cart_xpath = '//a[@class="b-link-popup"]'
    # Ссылка "Восстановить удалённое"
    cart_restore_xpath = '//a[@class="b-link-popup g-alttext-deepblue"]'
    # Кнопка "Отложенные"
    cart_deffered_xpath = '//a[@href="#step1-put"]'
    # Кнопка "Моя корзина"
    cart_mycart_xpath = '//a[@href="#step1-default"]'
    # Надпись "ОТЛОЖЕННЫЕ ТОВАРЫ"
    cart_deffered_goods_xpath = '//*[@id="step1-put"]/div[1]/div[1]'
    # Надпись "ВАШ ЗАКАЗ"
    cart_mycart_goods_xpath = '//*[@id="basket-step1-default"]/div[2]/span[1]'
    # Ссыдка "Сертификаты и купоны"
    cart_coupon_xpath = '//*[@id="basket-step1-default"]/div[5]/div[2]/span[1]/span[1]'
    # Поле ввода купона
    cart_coupon_input_xpath = '//input[@placeholder="КУПОН"]'
    # Кнопка "Применить" в окне с купоном
    cart_coupon_apply_button_xpath = '//div[@class="base-button--content"]'
