#!/usr/bin/python3
# -*- encoding=utf8 -*-
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class MainPage(NopCommerce):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    menu_li = "ul.top-menu.notmobile li a"

    # getters

    def get_menu(self):
        """ Получить все ссылки из меню 'Товары' с главной страницы сайта """
        return self.driver.find_elements(By.CSS_SELECTOR, self.menu_li)

    # actions

    def create_menu(self):
        menu = self.get_menu()

        dict_item_menu = {}
        flag = 0
        for _ in menu:
            if _.get_attribute('href').split('.com/')[1] not in ('computers', 'electronics', 'apparel'):
                dict_item_menu[flag] = [_.get_attribute('href').split('.com/')[1], _.get_attribute('href')]
                flag += 1

        return dict_item_menu

    # methods

    def show_menu_and_input_number(self):
        """ Возвращает ссылку на выбранную категорию товаров"""
        menu = self.create_menu()
        # выводим в консоль меню
        print("-> Меню: ")
        for k, v in menu.items():
            print(k, '-', v[0])
        # вводим нужный пункт меню
        number = input("-> Введите номер раздела меню: ")

        return menu[int(number)][1]
