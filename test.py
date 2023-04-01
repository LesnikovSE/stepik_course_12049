#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec


class NopCommerce:
    url = "https://demo.nopcommerce.com/"
    loc_menu = "ul.top-menu.notmobile li a"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def scroll_to_obj(self, obj):
        self.driver.execute_script("arguments[0].scrollIntoView();", obj)

    def get_menu(self) -> dict:
        """ Получить все ссылки из меню 'Товары' с главной страницы сайта """
        menu = self.driver.find_elements(By.CSS_SELECTOR, self.loc_menu)

        dict_item_menu = {}
        flag = 1
        for _ in menu:
            if _.get_attribute('href').split('.com/')[1] not in ('computers', 'electronics', 'apparel'):
                dict_item_menu[flag] = [_.get_attribute('href').split('.com/')[1], _.get_attribute('href')]
                flag += 1

        return dict_item_menu


if __name__ == '__main__':
    driver = Chrome()
    obj = NopCommerce(driver)
    obj.driver.get(obj.url)

    menu = obj.get_menu()

    print("-> Меню: ")
    for k, v in menu.items():
        print(k, '-', v[0])
    print("-> Введите номер интересующего раздела меню: ")
    # number = int(input())

    # obj.driver.get(menu[number][1])

