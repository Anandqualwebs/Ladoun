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
from Pages.profilePage import ProfilePage
from Pages.checkoutPage import CheckoutPage


class loginTest(unittest.TestCase):
    baseURL = "https://ladoun.com/customer/account/login/"
    correctemail = "testone@mailinator.com"
    correctpassword = 123456
    name = "Test Test"
    newpassword = 123456
    addressone = "box no."
    addresstwo = "23"
    phone = "123454322"
    country = "SA"
    state = 1
    city = "keddah"
    company = "qualwebs"
    fax = "123322"
    zip = "452003"

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    def test__change_password(self):
        driver = self.driver

        self.driver.get(self.baseURL)
        time.sleep(2)
        language = CheckoutPage(driver)
# English
        language.click_english()
        time.sleep(4)
#Login
        login = LoginPage(driver)
        login.enter_login_email(self.correctemail)
        login.enter_login_password(self.correctpassword)
        login.click_login()
        time.sleep(2)
        login.dashboard_visible_check()
        time.sleep(1)

        profile = ProfilePage(driver)
# change Password
        profile.click_change_password()
        time.sleep(2)
        profile.enter_current_password(self.correctpassword)
        profile.enter_new_password(self.newpassword)
        profile.enter_confirm_new_password(self.newpassword)
        profile.click_save()
        time.sleep(2)
        profile.password_changed_success_check()

    def test_change_name(self):
        driver = self.driver
        profile = ProfilePage(driver)
        profile.click_account_dashboard()
        time.sleep(2)
#Change name
        profile.click_change_name()
        time.sleep(3)
        profile.enter_name(self.name)
        profile.click_save()
        time.sleep(2)
        profile.password_changed_success_check()

    def test_add_new_address(self):
        driver = self.driver
        profile = ProfilePage(driver)
        profile.click_address_tab()
        time.sleep(2)
        profile.click_add_new_address()
        time.sleep(2)

        profile.enter_new_name(self.name)
        profile.enter_company_name(self.company)
        profile.enter_phone_number(self.phone)
        profile.enter_fax_number(self.fax)
        profile.enter_address_one(self.addressone)
        profile.enter_address_two(self.addresstwo)

        profile.select_new_country(self.country)
        time.sleep(3)
        profile.select_new_state(self.state)
        time.sleep(2)
        profile.enter_new_city_name(self.city)
        profile.enter_zip_number(self.zip)

        profile.click_billing_checkbox()
        profile.click_shipping_checkbox()
        profile.click_save_address()
        time.sleep(3)

    @classmethod
    def tearDownClass(inst):
     time.sleep(1)
     inst.driver.quit()
