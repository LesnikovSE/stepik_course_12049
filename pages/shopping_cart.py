#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class ShoppingCartPage(NopCommerce):
    checkbox_i_agree = "//input[@id='termsofservice']"
    btn_checkout = "//button[@id='checkout']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters

    def get_checkbox_i_agree(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_i_agree)))

    def get_btn_checkout(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.btn_checkout)))

    # action

    def click_i_agree(self):
        self.scroll_to_obj(self.get_checkbox_i_agree())
        self.get_checkbox_i_agree().click()
        print("click checkbox 'I agree'")

    def click_btn_checkbox(self):
        self.scroll_to_obj(self.get_btn_checkout())
        self.get_btn_checkout().click()
        print("click button 'Checkout'")
