class Locators:
    # login page objects
    username_textbox_name = 'login'
    password_textbox_name = 'password'
    login_button_class_name = 'auth_button'
    invalidUsername_message_css_selector = '#content-box > div > div'
    invalidPassword_message_css_selector = '#content-box > div > div'
    invalidUsernameAndPassword_css_selector = '#content-box > div > div'

    # home page objects
    '''welcome_css_selector = '#content-box > div > h2'
    click_my_tabs_css_selector = '#content-box > h1'
    my_tabs_link_text = 'Мои закладки'
    my_orders_link_text = 'Мои заказы'
    my_profile_link_text = 'Мой профиль'
    contact_link_text = 'Контактная информация'
    delivery_info_link_text = 'Информация о доставке'
    other_info_link_text = 'Дополнительная информация'
    change_password_link_text = 'Сменить пароль'
    new_password_class_name = 'password'
    confirmation_new_password_class_name = 'is_password'
    old_password_class_name = 'old_password'
    exit_link_text = 'Выход'
    basket_id = 'basket'
    catalog_products_class_name = 'catalog-list-menu'
    new_products_xpath = '//*[@id="menu"]/div/span[5]/a'
    sale_xpath = '//*[@id="menu"]/div/span[6]/a'
    discounts_and_bonuses_xpath = '//*[@id="menu"]/div/span[7]/a'
    payment_and_delivery_xpath = '//*[@id="menu"]/div/span[8]/a'
    hurry_up_xpath = '//*[@id="menu"]/div/span[9]/a'
    contacts_xpath = '//*[@id="menu"]/div/span[10]/a'
    airsoft_guns_xpath = '//*[@id="menu"]/div/div/div/ul/li[1]/a'
    all_guns_xpath = '//*[@id="left_box"]/div[1]/div[2]/div[3]/a[4]'
    pyrotechnics_xpath = '//*[@id="menu"]/div/div/div/ul/li[4]/a'
    all_guns_xpath_2 = '//*[@id="left_box"]/div[1]/div[2]/div[3]/a[4]'
    link_vk_xpath = '//*[@id="content-left"]/div[2]/a[1]'
    link_facebook_xpath = '//*[@id="content-left"]/div[2]/a[2]'
    link_twitter_xpath = '//*[@id="content-left"]/div[2]/a[3]'
    link_instagram_xpath = '//*[@id="content-left"]/div[2]/a[4]'
    link_youtube_xpath = '//*[@id="content-left"]/div[2]/a[5]'
    link_telegram_bot_xpath = '//*[@id="content-left"]/div[2]/a[6]'
    email_us_css_selector = '#footer > div.center > div.office > div > div.call-back-footer > a'
    close_the_form_css_selector = 'body > div.fancybox-wrap.fancybox-desktop.fancybox-type-iframe.fancybox-opened > div > div.fancybox-item.fancybox-close'
    articles_xpath = '//*[@id="footer"]/div[1]/div[2]/ul/li[4]/a'
    top_logo_css_selector = '#logo > a'
    button_buy_vint1_xpath = '//*[@id="indicator_catalog"]/div[1]/div[1]/div/button[1]'
    '''

    ##############################ТУТ НАЧИНАЮТСЯ ЛОКАТОРЫ ЛАБИРИНТА####################################
    my_lab_button_xpath = '//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]/span[1]/span[1]/span[1]'
    messages_button_xpath = '//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/span[1]/span[1]/span[1]'
    main_menu_xpath = '//ul[@class = "b-header-b-personal-e-list ul-justify"]/li'
    cookie_policy_botton_xpath = '//button[@class="cookie-policy__button js-cookie-policy-agree"]'
    login_input_xpath = '//input'
    authorization_button_xpath = '//*[@id="g-recap-0-btn"]'
    discount_code_xpath = "//input[@name='code']"
    authorization_email_sent_button_xpath = '//*[@id="auth-email-sent"]/input[5]'
    succesfull_login_popup_xpath = "//span[@class='popup-nib-tip']"
    logout_link_xpath = '//a[@class="user-top-menu-link user-top-menu-link_logout"]'
    discount_code_div_xpath = "//div[@class='max-width discount-code']"
    search_field_xpath = '//*[@id="search-field"]'
    search_button_xpath = "//button[@class='b-header-b-search-e-btn']"
    search_result_xpath = '//*[@id="stab-slider-frame"]/ul[1]/li[1]'
    labirint_logo_xpath = '//a[@class="b-header-b-logo-e-logo-wrap"]'
    messages_xpath = '//span[@class="b-header-b-personal-e-icon-wrapper"]'
    top_menu_xpath = "//span[@class='b-header-b-personal-e-wrapper-m-closed']"
    labirint_now_xpath = '//a[@href="/now"]'
    labirint_best_xpath = '//a[@href="/best/"]'
    cart_create_order_xpath = '//a[@title="Оформить заказ"]'
    empty_cart_xpath = '//*[@id="basket-step1-default"]/div[1]/span'
    users_agreement_xpath = "//a[@href='/agreement/']"
    books_button_xpath = "//a[@href='/books/']"
    books_comix_xpath = "//span[@class='b-menu-list-title b-menu-list-title-first']"
    books_gameworld_xpath = "//a[@href='/genres/2994']"
    school_button_xpath = "//a[@href='/school/']"
    school_predmet_english_xpath = '//a[@href="/school/?predmet[]=4#right"]'
    games_button_xpath = '//a[@href="/games/"]'
    children_art_xpath = '//*[@id="header-toys"]/div[1]/ul[1]/li[3]/span[1]'
    diamonds_mozaic_xpath = '//a[@href="/genres/3339"]'
    stationery_xpath = "//a[@href='/office/']"
    globus_xpath = "//a[@href = '/genres/1500']"
    mainmenu_submenu_xpath = '//span[@class="b-header-b-menu-e-text"]'
    multimedia_xpath = "//a[@href='/multimedia/']"
    souvenir_xpath = "//a[@href='/souvenir/']"
    journals_xpath = "//a[@href='/journals/']"
    household_xpath = "//a[@href='/household/']"
    club_xpath = "//a[@href='/club/']"
    region_xpath = '//span[@class="region-location-icon-txt "]'
    region_input_xpath = '//input[@id="region-post"]'
    map_xpath = '//a[@href="/maps/"]'
    delivery_date_filter_xpath = '//*[@id="js-delivery-date-filter"]'
    delevery_dates_select_all_xpath = '//*[@id="delivery-dates-popup-window"]/div[2]/div[1]'
    delivery_point_caption_xpath = '//div[@class = "delivery-point__caption"]'
    delivery_point_ymaps_xpath = '//*[@id="delivery-point-map"]/ymaps/ymaps/ymaps/ymaps[7]/ymaps/ymaps/ymaps/ymaps[1]/ymaps[2]'
    delivery_and_paymen_button_xpath = '//a[@class ="b-header-b-sec-menu-e-link"]'

    cart_clear_cart_xpath = '//a[@class="b-link-popup"]'
    cart_restore_xpath = '//a[@class="b-link-popup g-alttext-deepblue"]'
    cart_deffered_xpath = '//a[@href="#step1-put"]'
    cart_mycart_xpath = '//a[@href="#step1-default"]'
    cart_deffered_goods_xpath = '//*[@id="step1-put"]/div[1]/div[1]'
    cart_mycart_goods_xpath = '//*[@id="basket-step1-default"]/div[2]/span[1]'
    cart_coupon_xpath = '//*[@id="basket-step1-default"]/div[5]/div[2]/span[1]/span[1]'
    cart_coupon_input_xpath = '//input[@placeholder="КУПОН"]'
    cart_coupon_apply_button_xpath = '//div[@class="base-button--content"]'