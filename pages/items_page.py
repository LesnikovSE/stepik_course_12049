#!/usr/bin/python3
# -*- encoding=utf8 -*-
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class ItemsPage(NopCommerce):
    items = "div.product-item"
    btn_add_to_cart = "//button[text()='Add to cart']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters

    def get_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.items)

    def get_buttons(self):
        return self.driver.find_elements(By.XPATH, self.btn_add_to_cart)

    def create_menu(self):
        items = self.get_items()

        dict_items = {}
        flag = 0
        for item in items:
            name = item.find_element(By.CSS_SELECTOR, 'h2.product-title')
            dict_items[flag] = name.text
            flag += 1
        return dict_items

    # action

    def add_item_to_cart(self, number_item):
        self.scroll_to_obj(self.get_buttons()[number_item])
        self.get_buttons()[number_item].click()

    def close_popup_info_block(self):
        self.driver.find_element(By.CSS_SELECTOR, 'span.close').click()

    # method

    def show_menu_and_return_number(self):
        dict_items = self.create_menu()
        # выводим в консоль меню
        print("-> Меню: ")
        for k, v in dict_items.items():
            print(k, '-', v)
        # вводим нужный пункт меню
        number = input("-> Введите номер товара: ")
        return int(number)
