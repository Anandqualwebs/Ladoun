from selenium.webdriver.support.select import Select
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.locators import locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.enter_email_xpath = locators.enter_email_xpath
        self.enter_password_xpath = locators.enter_password_xpath
        self.click_login_xpath = locators.click_login_xpath
        self.dashboard_xpath = locators.dashboard_xpath
        self.invalid_credential_error_xpath = locators.invalid_credential_error_xpath
        self.logout_xpath = locators.logout_xpath
        self.click_forgot_password_xpath = locators.click_forgot_password_xpath
        self.enter_forgot_email_xpath = locators.enter_forgot_email_xpath
        self.click_reset_password_xpath = locators.click_reset_password_xpath
        self.reset_email_sent_xpath = locators.reset_email_sent_xpath
        self.create_account_button_xpath = locators.create_account_button_xpath
        self.create_account_name_xpath = locators.create_account_name_xpath
        self.create_account_email_xpath = locators.create_account_email_xpath
        self.create_account_password_xpath = locators.create_account_password_xpath
        self.create_account_con_password_xpath = locators.create_account_con_password_xpath
        self.create_account_submit_xpath = locators.create_account_submit_xpath

#Create Account

    def click_create_account(self):
        self.driver.find_element_by_xpath(self.create_account_button_xpath).click()

    def enter_create_name(self, name):
        self.driver.find_element_by_xpath(self.create_account_name_xpath).clear()
        self.driver.find_element_by_xpath(self.create_account_name_xpath).send_keys(name)

    def enter_create_email(self, email):
        self.driver.find_element_by_xpath(self.create_account_email_xpath).clear()
        self.driver.find_element_by_xpath(self.create_account_email_xpath).send_keys(email)

    def enter_create_password(self, password):
        self.driver.find_element_by_xpath(self.create_account_password_xpath).clear()
        self.driver.find_element_by_xpath(self.create_account_password_xpath).send_keys(password)

    def enter_create_con_password(self, conpassword):
        self.driver.find_element_by_xpath(self.create_account_con_password_xpath).clear()
        self.driver.find_element_by_xpath(self.create_account_con_password_xpath).send_keys(conpassword)

    def click_create_submit(self):
        self.driver.find_element_by_xpath(self.create_account_submit_xpath).click()

#login

    def enter_login_email(self, email):
        self.driver.find_element_by_xpath(self.enter_email_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_email_xpath).send_keys(email)

    def enter_login_password(self, password):
        self.driver.find_element_by_xpath(self.enter_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.click_login_xpath).click()

#dashboard validation

    def dashboard_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.dashboard_xpath).is_displayed()
        print("Dashboard Is Displayed ? = ", element1)

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()


#Error
    def invalid_credential_error_check(self):
        element1 = self.driver.find_element_by_xpath(self.invalid_credential_error_xpath).is_displayed()
        print("Invalid id pass Error Is Displayed ? = ", element1)


#Forgot Password

    def click_forgot_password(self):
        self.driver.find_element_by_xpath(self.click_forgot_password_xpath).click()

    def enter_forgot_email(self, email):
        self.driver.find_element_by_xpath(self.enter_forgot_email_xpath).send_keys(email)

    def click_reset_password(self):
        self.driver.find_element_by_xpath(self.click_reset_password_xpath).click()

    def reset_email_sent_check(self):
        element1 = self.driver.find_element_by_xpath(self.reset_email_sent_xpath).is_displayed()
        print("Reset password link Sent Is Displayed = ", element1)

