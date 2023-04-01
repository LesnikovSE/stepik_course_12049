#!/usr/bin/python3
# -*- encoding=utf8 -*-
# import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By

from pages.ch_sppc import SPPCPage
from pages.checkout_as_guest import CheckoutAsGuestPage
from pages.ch_billing_adress import BillingAddressPage
from pages.main_page import MainPage
from pages.items_page import ItemsPage
from pages.shopping_cart import ShoppingCartPage


def test_purchase_of_one_product_without_registration():
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = Chrome(chrome_options=options)
    driver.get('https://demo.nopcommerce.com/')

    # Заходим на главную страницу магазина
    mp = MainPage(driver)
    print(mp.get_current_url())
    # переходим на страницу с товарами выбранной категории
    link = mp.show_menu_and_input_number()
    driver.get(link)
    #
    itp = ItemsPage(driver)
    print(itp.get_current_url())
    # выводим в консоль меню с товарами и вводим номер товара
    menu = itp.create_menu()
    number = itp.show_menu_and_return_number()
    print(f"Товар '{menu[number]}' добавлен в корзину")
    # Добавляем указанный товар в корзину
    itp.add_item_to_cart(number)
    # Прокручиваем вверх страницы
    itp.scroll_up()
    sleep(1)
    # закрыть всплывающее оповещение о добавленном товаре
    itp.close_popup_info_block()
    sleep(1)
    # переходим в корзину
    itp.click_cart()
    # подтвердить покупку и нажать checkout
    scp = ShoppingCartPage(driver)
    scp.get_current_url()
    scp.click_i_agree()
    scp.click_btn_checkbox()
    # продолжить покупку без регистрации как гость
    cagp = CheckoutAsGuestPage(driver)
    cagp.get_current_url()
    cagp.click_btn_checkoutAsGuest()
    # billing address
    bap = BillingAddressPage(driver)
    bap.input_address()
    bap.get_btn_continue().click()

    # sppc - ship method, pay method, pay info, conf order
    sppc = SPPCPage(driver)
    # shipping
    # use 3 radio button
    sppc.get_current_url()
    sppc.get_ship_radio_btn("1").click()
    sppc.get_ship_btn_continue().click()
    # payment method
    # use 2 radio button - money order/ credit card
    sppc.get_current_url()
    sppc.get_pay_radio_btn("0").click()
    sppc.get_pay_btn_continue().click()
    # payment info
    sppc.get_current_url()
    sppc.get_pay_info_btn_continue().click()
    # Confirm order
    sppc.get_current_url()
    sppc.scroll_to_obj(sppc.get_conf_order_btn_continue())
    sppc.get_conf_order_btn_continue().click()
    # Your order has been successfully processed!
    print(sppc.driver.find_element(By.CSS_SELECTOR, 'div.order-number').text)

    driver.close()
