#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class SPPCPage(NopCommerce):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    ship_radio_btn = f"//input[@id='shippingoption_" + "{}" + "']"
    ship_btn_continue = "//button[@class='button-1 shipping-method-next-step-button']"

    pay_radio_btn = f"//input[@id='paymentmethod_" + "{}" + "']"
    pay_btn_continue = "//button[@class='button-1 payment-method-next-step-button']"

    pay_info_btn_continue = "//button[@class='button-1 payment-info-next-step-button']"

    conf_order_btn_continue = "//button[@class='button-1 confirm-order-next-step-button']"

    # Shipping method radio button

    def get_ship_radio_btn(self, value: str):
        btn = self.ship_radio_btn.format(value)
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, btn)))

    # Payment method radio button
    def get_pay_radio_btn(self, value: str):
        btn = self.pay_radio_btn.format(value)
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, btn)))

    # Shipping
    def get_ship_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.ship_btn_continue)))

    # Payment
    def get_pay_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.pay_btn_continue)))

    # Payment info
    def get_pay_info_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.pay_info_btn_continue)))

    # Confirm order
    def get_conf_order_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.conf_order_btn_continue)))
