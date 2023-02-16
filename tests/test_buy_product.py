import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

from pages.cart_page import Cart_page
from pages.client_page import Client_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.order(3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up):
    # options = Options()

    driver = webdriver.Firefox(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\geckodriver.exe')

    print("Start test 1")

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    bh = Finish_page(driver)
    bh.finish()

    print("Finish Test 1")
    # time.sleep(10)
    driver.quit()


# @pytest.mark.order(1)
@allure.description("Test buy product 2")
def test_buy_product_2(set_up):
    # options = Options()

    driver = webdriver.Firefox(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\geckodriver.exe')

    print("Start test 2 ")

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    bh = Finish_page(driver)
    bh.finish()

    print("Finish Test 2")
    # time.sleep(10)
    driver.quit()


# @pytest.mark.order(2)
@allure.description("Test buy product 3")
def test_buy_product_3(set_up):
    # options = Options()

    driver = webdriver.Firefox(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\geckodriver.exe')

    print("Start test 3")

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    bh = Finish_page(driver)
    bh.finish()

    print("Finish Test 3")
    # time.sleep(10)
    driver.quit()
