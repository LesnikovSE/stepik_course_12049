#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec

from pages.base import NopCommerce


class BillingAddressPage(NopCommerce):
    # url = "https://demo.nopcommerce.com/onepagecheckout#opc-billing"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    first_name = "//input[@id='BillingNewAddress_FirstName']"
    last_name = "//input[@id='BillingNewAddress_LastName']"
    email = "//input[@id='BillingNewAddress_Email']"
    company = "//input[@id='BillingNewAddress_Company']"

    country = "//select[@id='BillingNewAddress_CountryId']"
    state = "//select[@id='BillingNewAddress_StateProvinceId']"

    city = "//input[@id='BillingNewAddress_City']"
    address_1 = "//input[@id='BillingNewAddress_Address1']"
    address_2 = "//input[@id='BillingNewAddress_Address2']"
    zip = "//input[@id='BillingNewAddress_ZipPostalCode']"
    phone = "//input[@id='BillingNewAddress_PhoneNumber']"
    fax = "//input[@id='BillingNewAddress_FaxNumber']"

    btn_continue = "//button[@class='button-1 new-address-next-step-button']"

    # Getters

    def get_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.btn_continue)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.email)))

    def get_company(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.company)))

    def get_select_country(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.country)))

    # select
    def get_select_state(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.state)))

    # select
    def get_city(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.city)))

    def get_address_1(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.address_1)))

    def get_address_2(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.address_2)))

    def get_zip(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.zip)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.phone)))

    def get_fax(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.fax)))

    # Actions

    def input_first_name(self, value):
        self.get_first_name().send_keys(value)
        print("Input first name")

    def input_last_name(self, value):
        self.get_last_name().send_keys(value)
        print("Input last name")

    def input_email(self, value):
        self.get_email().send_keys(value)
        print("Input email")

    def input_company(self, value):
        self.get_company().send_keys(value)
        print("Input company")

    # select
    def country_select_by_value(self, value):
        Select(self.get_select_country()).select_by_value(value)

    # select
    def state_select_by_value(self, value):
        Select(self.get_select_state()).select_by_value(value)

    def input_city(self, value):
        self.get_city().send_keys(value)
        print("Input city")

    def input_address_1(self, value):
        self.get_address_1().send_keys(value)
        print("Input address_1")

    def input_address_2(self, value):
        self.get_address_2().send_keys(value)
        print("Input address_2")

    def input_zip(self, value):
        self.get_zip().send_keys(value)
        print("Input zip")

    def input_phone(self, value):
        self.get_phone().send_keys(value)
        print("Input phone")

    def input_fax(self, value):
        self.get_fax().send_keys(value)
        print("Input fax")

    # Methods

    def input_address(self):
        self.input_first_name("test_first_name")
        self.input_last_name("test_last_name")
        self.input_email("test_mail@mail.ru")
        self.scroll_to_obj(self.get_company())
        self.input_company("test_company")
        self.scroll_to_obj(self.get_select_country())
        self.country_select_by_value("219")
        self.scroll_to_obj(self.get_select_state())
        # self.state_select_by_value("")
        self.scroll_to_obj(self.get_city())
        self.input_city("test_city")
        self.scroll_to_obj(self.get_address_1())
        self.input_address_1("test_address1")
        self.scroll_to_obj(self.get_address_2())
        self.input_address_2("test_address2")
        self.scroll_to_obj(self.get_zip())
        self.input_zip("test_zip")
        self.scroll_to_obj(self.get_phone())
        self.input_phone("+79990000000")
        self.scroll_to_obj(self.get_fax())
        self.input_fax("test_fax")
