#!/usr/bin/python3
# -*- encoding=utf8 -*-
from datetime import datetime
# from time import sleep
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class NopCommerce:
    cart = "//a[@class='ico-cart']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def scroll_to_obj(self, obj):
        self.driver.execute_script("arguments[0].scrollIntoView();", obj)

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    def get_current_url(self):
        """ method get current url """
        print(f"-> Current url: {self.driver.current_url} <-")

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d %H.%M.%S")
        name_scr = "screenshot" + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\GM\\PycharmProjects\\nopcommerce\\screenshot\\' + name_scr)
        print("-> Screenshot create <-")

    # CART

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.cart)))

    def click_cart(self):
        self.get_cart().click()
        print("go to 'Shopping Cart'")