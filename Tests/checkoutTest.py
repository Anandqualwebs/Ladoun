import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.checkoutPage import CheckoutPage
from Pages.loginPage import LoginPage


class checkoutTest(unittest.TestCase):
    productURL = "https://ladoun.com/lm5012.html"
    checkoutURL = "https://ladoun.com/onestep"
    loginURL = "https://ladoun.com/customer/account/login/"
    name  = "Test Test"
    address = "box no. 23"
    phone = "123454322"
    country = "SA"
    state = 1
    city = 2
    cardname = "Test Test"
    cardnumber = 4242424242424242
    month = 3
    year = 3
    cardcvv = 123
    correctemail = "testone@mailinator.com"
    correctpassword = 123456

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    def test_user_Checkout(self):
        driver = self.driver
# LoginUrl
        self.driver.get(self.loginURL)
        time.sleep(3)

        checkout = CheckoutPage(driver)
#English
        checkout.click_english()
        time.sleep(4)
#Login
        login = LoginPage(driver)
        login.enter_login_email(self.correctemail)
        login.enter_login_password(self.correctpassword)
        login.click_login()
        time.sleep(3)
#Product
        self.driver.get(self.productURL)
#Product
        time.sleep(4)
        checkout.click_addcart()
        time.sleep(3)
        self.driver.get(self.checkoutURL)
        time.sleep(3)
#Details
        checkout.enter_name(self.name)
        checkout.enter_address(self.address)
        checkout.select_country(self.country)
        time.sleep(3)
        checkout.select_state(self.state)
        time.sleep(3)
        checkout.select_city(self.city)
        time.sleep(2)
        checkout.enter_phone(self.phone)
        time.sleep(2)
        checkout.click_verify()
        time.sleep(2)
        checkout.click_verify()
        time.sleep(4)
        checkout.click_verify_otp()
        time.sleep(8)
#Card
        checkout.enter_card_number(self.cardnumber)
        checkout.enter_card_name(self.cardname)
        checkout.enter_card_cvv(self.cardcvv)
        checkout.select_month(self.month)
        checkout.select_year(self.year)
#Cod
        #checkout.click_cod()
        #time.sleep(5)

#Place Order
        checkout.click_place_order()
        time.sleep(6)

    def test_guest_Checkout(self):

        driver = self.driver
        checkout = CheckoutPage(driver)

# Product
        self.driver.get(self.productURL)
# English
        checkout.click_english()
# Product
        time.sleep(4)
        checkout.click_addcart()
        time.sleep(3)
        self.driver.get(self.checkoutURL)
        time.sleep(3)
# Details
        checkout.click_no_email()
        time.sleep(3)
        checkout.enter_name(self.name)
        checkout.enter_address(self.address)
        checkout.select_country(self.country)
        time.sleep(3)
        checkout.select_state(self.state)
        time.sleep(3)
        checkout.select_city(self.city)
        time.sleep(2)
        checkout.enter_phone(self.phone)
        time.sleep(2)
        checkout.click_verify()
        time.sleep(2)
        checkout.click_verify()
        time.sleep(4)
        checkout.click_verify_otp()
        time.sleep(10)
# Card
        checkout.enter_card_number(self.cardnumber)
        checkout.enter_card_name(self.cardname)
        checkout.enter_card_cvv(self.cardcvv)
        checkout.select_month(self.month)
        checkout.select_year(self.year)
# Cod
        #checkout.click_cod()
        #time.sleep(5)

# Place Order
        checkout.click_place_order()
        time.sleep(6)

    @classmethod
    def tearDownClass(inst):
     time.sleep(90)
     inst.driver.quit()

