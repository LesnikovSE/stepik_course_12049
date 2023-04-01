#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class CheckoutAsGuestPage(NopCommerce):
    url = "https://demo.nopcommerce.com/login/checkoutasguest?returnUrl=%2Fcart"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    btn_checkoutAsGuest = "//button[@class='button-1 checkout-as-guest-button']"

    # getters

    def get_btn_checkoutAsGuest(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.btn_checkoutAsGuest)))

    # actions

    def click_btn_checkoutAsGuest(self):
        self.get_btn_checkoutAsGuest().click()
        print("Input user name")
