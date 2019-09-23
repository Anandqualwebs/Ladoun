from selenium.webdriver.support.select import Select
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.locators import locators

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.eng_change_xpath = locators.eng_change_xpath
        self.add_cart_product_xpath = locators.add_cart_product_xpath
        self.no_email_xpath = locators.no_email_xpath
        self.name_xpath = locators.name_xpath
        self.address_xpath = locators.address_xpath
        self.phone_xpath = locators.phone_xpath
        self.select_country_xpath = locators.select_country_xpath
        self.select_state_xpath = locators.select_state_xpath
        self.select_city_xpath = locators.select_city_xpath
        self.click_verify_xpath = locators.click_verify_xpath
        self.click_verify_otp_xpath = locators.click_verify_otp_xpath
        self.enter_card_name_xpath = locators.enter_card_name_xpath
        self.enter_card_number_xpath = locators.enter_card_number_xpath
        self.enter_card_cvv_xpath = locators.enter_card_cvv_xpath
        self.select_month_xpath = locators.select_month_xpath
        self.select_year_xpath = locators.select_year_xpath
        self.click_place_order_xpath = locators.click_place_order_xpath
        self.click_cod_xpath = locators.click_cod_xpath


    def click_english(self):
        self.driver.find_element_by_xpath(self.eng_change_xpath).click()

    def click_addcart(self):
        self.driver.find_element_by_xpath(self.add_cart_product_xpath).click()

    def click_no_email(self):
        self.driver.find_element_by_xpath(self.no_email_xpath).click()

    def enter_name(self, name):
        self.driver.find_element_by_xpath(self.name_xpath).clear()
        self.driver.find_element_by_xpath(self.name_xpath).send_keys(name)

    def enter_address(self, address):
        self.driver.find_element_by_xpath(self.address_xpath).clear()
        self.driver.find_element_by_xpath(self.address_xpath).send_keys(address)

    def enter_phone(self, phone):
        self.driver.find_element_by_xpath(self.phone_xpath).clear()
        self.driver.find_element_by_xpath(self.phone_xpath).send_keys(phone)

    def select_country(self, country):
       Select(self.driver.find_element_by_xpath(self.select_country_xpath)).select_by_value(country)

    def select_state(self, state):
       Select(self.driver.find_element_by_xpath(self.select_state_xpath)).select_by_index(state)

    def select_city(self, city):
       Select(self.driver.find_element_by_xpath(self.select_city_xpath)).select_by_index(city)

    def click_verify(self):
        self.driver.find_element_by_xpath(self.click_verify_xpath).click()

    def click_verify_otp(self):
        self.driver.find_element_by_xpath(self.click_verify_otp_xpath).click()

    def enter_card_name(self, cardname):
        self.driver.find_element_by_xpath(self.enter_card_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_card_name_xpath).send_keys(cardname)

    def enter_card_number(self, cardnumber):
        self.driver.find_element_by_xpath(self.enter_card_number_xpath).send_keys(cardnumber)

    def enter_card_cvv(self, cardcvv):
        self.driver.find_element_by_xpath(self.enter_card_cvv_xpath).send_keys(cardcvv)

    def select_month(self, month):
       Select(self.driver.find_element_by_xpath(self.select_month_xpath)).select_by_index(month)

    def select_year(self, year):
       Select(self.driver.find_element_by_xpath(self.select_year_xpath)).select_by_index(year)

    def click_cod(self):
        self.driver.find_element_by_xpath(self.click_cod_xpath).click()

    def click_place_order(self):
        self.driver.find_element_by_xpath(self.click_place_order_xpath).click()


