import time

import allure
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

@allure.description("Test link about")
def test_link_about(set_up):

    driver = webdriver.Firefox(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\geckodriver.exe')

    print("Start test")

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")
    # time.sleep(10)
    driver.quit()





