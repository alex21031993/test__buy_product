import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Client_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    button_continue = "//input[@id='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("input postal code")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click button continue")

    # Methods
    def input_information(self):
        with allure.step("Input information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.input_first_name("Ivanov")
            self.input_last_name("Ivan")
            self.input_postal_code("asd")
            self.click_button_continue()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")
