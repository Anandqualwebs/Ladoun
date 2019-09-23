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
from Pages.loginPage import LoginPage
from Pages.checkoutPage import CheckoutPage


class loginTest(unittest.TestCase):
    baseURL = "https://ladoun.com/customer/account/login/"
    correctemail = "testone@mailinator.com"
    correctpassword = 123456
    incorrectemail1 = "testone@mailinator.com"
    incorrectpassword1 = 123123
    incorrectemail2 = "ttestone@mailinator.com"
    incorrectpassword2 = 2123123
    newname = "Test Test"
    newemail = "testnew1@mailinator.com"

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    def test__correct_Login(self):
        driver = self.driver

        self.driver.get(self.baseURL)
        time.sleep(2)

        language = CheckoutPage(driver)
# English
        language.click_english()
        time.sleep(4)

        login = LoginPage(driver)
        login.enter_login_email(self.correctemail)
        login.enter_login_password(self.correctpassword)
        login.click_login()
        time.sleep(2)
        login.dashboard_visible_check()
        time.sleep(1)
        login.click_logout()
        time.sleep(1)

    def test_incorrect_Login__one(self):
        driver = self.driver

        self.driver.get(self.baseURL)
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_login_email(self.incorrectemail1)
        login.enter_login_password(self.incorrectpassword1)
        login.click_login()
        time.sleep(2)
        login.invalid_credential_error_check()

    def test_incorrect_Login_two(self):
        driver = self.driver

        self.driver.get(self.baseURL)
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_login_email(self.incorrectemail2)
        login.enter_login_password(self.incorrectpassword2)
        login.click_login()
        time.sleep(2)

        login.invalid_credential_error_check()

    def test_forgot_password(self):
        driver = self.driver

        self.driver.get(self.baseURL)
        time.sleep(2)

        forgot = LoginPage(driver)
        forgot.click_forgot_password()
        time.sleep(2)
        forgot.enter_forgot_email(self.correctemail)
        time.sleep(10)
        forgot.click_reset_password()
        time.sleep(2)
        forgot.reset_email_sent_check()


    # def test_registration(self):
    #     driver = self.driver
    #     self.driver.get(self.baseURL)
    #     time.sleep(2)
    #     regis = LoginPage(driver)
    #     regis.click_create_account()
    #     time.sleep(2)
    #     regis.enter_create_name(self.newname)
    #     regis.enter_create_email(self.newemail)
    #     regis.enter_create_password(self.correctpassword)
    #     regis.enter_create_con_password(self.correctpassword)
    #     time.sleep(10)
    #     regis.click_create_submit()
    #     time.sleep(2)
    #     regis.dashboard_visible_check()



    @classmethod
    def tearDownClass(inst):
     time.sleep(1)
     inst.driver.quit()
