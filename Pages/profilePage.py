from selenium.webdriver.support.select import Select
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.locators import locators

class ProfilePage():

    def __init__(self, driver):
        self.driver = driver

        self.click_account_dashboard_link_text = locators.click_account_dashboard_link_text
        self.click_change_pass_xpath = locators.click_change_pass_xpath
        self.click_change_pass_xpath = locators.click_change_pass_xpath
        self.enter_name_xpath = locators.enter_name_xpath
        self.enter_current_password_xpath = locators.enter_current_password_xpath
        self.enter_new_password_xpath = locators.enter_new_password_xpath
        self.enter_confirm_new_password_xpath = locators.enter_confirm_new_password_xpath
        self.click_save_xpath = locators.click_save_xpath
        self.password_changed_success_msg_xpath = locators.password_changed_success_msg_xpath
        self.click_change_name_xpath = locators.click_change_name_xpath

        self.click_address_tab_link_text = locators.click_address_tab_link_text
        self.click_add_new_address_xpath = locators.click_add_new_address_xpath
        self.enter_new_name_xpath = locators.enter_new_name_xpath
        self.enter_company_xpath = locators.enter_company_xpath
        self.enter_phone_xpath = locators.enter_phone_xpath
        self.enter_fax_xpath = locators.enter_fax_xpath
        self.enter_street_address_one = locators.enter_street_address_one
        self.enter_street_address_two = locators.enter_street_address_two
        self.select_new_country_xpath = locators.select_new_country_xpath
        self.select_new_state_xpath = locators.select_new_state_xpath
        self.enter_new_city_xpath = locators.enter_new_city_xpath
        self.enter_zip_xpath = locators.enter_zip_xpath
        self.billing_address_checkbox_xpath = locators.billing_address_checkbox_xpath
        self.shipping_address_checkbox_xpath = locators.shipping_address_checkbox_xpath
        self.click_save_address_xpath = locators.click_save_address_xpath



    def click_account_dashboard(self):
        self.driver.find_element_by_link_text(self.click_account_dashboard_link_text).click()

    def click_change_password(self):
        self.driver.find_element_by_xpath(self.click_change_pass_xpath).click()

    def enter_name(self, name):
        self.driver.find_element_by_xpath(self.enter_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_name_xpath).send_keys(name)

    def enter_current_password(self, password):
        self.driver.find_element_by_xpath(self.enter_current_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_current_password_xpath).send_keys(password)

    def enter_new_password(self, password):
        self.driver.find_element_by_xpath(self.enter_new_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_new_password_xpath).send_keys(password)

    def enter_confirm_new_password(self, password):
        self.driver.find_element_by_xpath(self.enter_confirm_new_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_confirm_new_password_xpath).send_keys(password)

    def click_save(self):
        self.driver.find_element_by_xpath(self.click_save_xpath).click()

    def password_changed_success_check(self):
        element1 = self.driver.find_element_by_xpath(self.password_changed_success_msg_xpath).is_displayed()
        print("Details Changed success msg Is Displayed = ", element1)

    def click_change_name(self):
        self.driver.find_element_by_xpath(self.click_change_name_xpath).click()

    def click_address_tab(self):
        self.driver.find_element_by_link_text(self.click_address_tab_link_text).click()

    def click_add_new_address(self):
        self.driver.find_element_by_xpath(self.click_add_new_address_xpath).click()

    def enter_new_name(self, password):
        self.driver.find_element_by_xpath(self.enter_new_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_new_name_xpath).send_keys(password)

    def enter_company_name(self, password):
        self.driver.find_element_by_xpath(self.enter_company_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_company_xpath).send_keys(password)

    def enter_phone_number(self, password):
        self.driver.find_element_by_xpath(self.enter_phone_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_phone_xpath).send_keys(password)

    def enter_fax_number(self, password):
        self.driver.find_element_by_xpath(self.enter_fax_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_fax_xpath).send_keys(password)

    def enter_address_one(self, password):
        self.driver.find_element_by_xpath(self.enter_street_address_one).clear()
        self.driver.find_element_by_xpath(self.enter_street_address_one).send_keys(password)

    def enter_address_two(self, password):
        self.driver.find_element_by_xpath(self.enter_street_address_two).clear()
        self.driver.find_element_by_xpath(self.enter_street_address_two).send_keys(password)


    def select_new_country(self, country):
       Select(self.driver.find_element_by_xpath(self.select_new_country_xpath)).select_by_value(country)

    def select_new_state(self, state):
       Select(self.driver.find_element_by_xpath(self.select_new_state_xpath)).select_by_index(state)

    def enter_new_city_name(self, password):
        self.driver.find_element_by_xpath(self.enter_new_city_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_new_city_xpath).send_keys(password)



    def enter_zip_number(self, password):
        self.driver.find_element_by_xpath(self.enter_zip_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_zip_xpath).send_keys(password)

    def click_billing_checkbox(self):
        self.driver.find_element_by_xpath(self.billing_address_checkbox_xpath).click()

    def click_shipping_checkbox(self):
        self.driver.find_element_by_xpath(self.shipping_address_checkbox_xpath).click()

    def click_save_address(self):
        self.driver.find_element_by_xpath(self.click_save_address_xpath).click()