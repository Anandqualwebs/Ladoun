from selenium.webdriver.support.select import Select
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.locators import locators

class ProductPage():

    def __init__(self, driver):
        self.driver = driver

        self.product_side_images_check_xpath = locators.product_side_images_check_xpath
        self.Product_main_images_check_xpath = locators.Product_main_images_check_xpath
        self.product_code_avail_check_xpath = locators.product_code_avail_check_xpath
        self.product_quantity_enter_xpath = locators.product_quantity_enter_xpath
        self.product_add_to_cart_click_xpath = locators.product_add_to_cart_click_xpath
        self.product_like_click_xpath = locators.product_like_click_xpath
        self.product_details_click_xpath = locators.product_details_click_xpath
        self.product_more_info_click_xpath = locators.product_more_info_click_xpath
        self.product_more_info_refer_check_xpath = locators.product_more_info_refer_check_xpath
        self.product_review_click_xpath = locators.product_review_click_xpath
        self.product_review_text_click_xpath = locators.product_review_text_click_xpath
        self.product_review_refer_check_xpath = locators.product_review_text_refer_check_xpath


    def side_images_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_side_images_check_xpath).is_displayed()
        print("Side Images Are Displayed ? = ", element1)

    def main_images_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.Product_main_images_check_xpath).is_displayed()
        print("Main Image Is Displayed ? = ", element1)

    def code_avail_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_code_avail_check_xpath).is_displayed()
        print("product code & availability Is Displayed ? = ", element1)

    def quantity_input_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_quantity_enter_xpath).is_displayed()
        element2 = self.driver.find_element_by_xpath(self.product_quantity_enter_xpath).is_enabled()
        print("Quantity input Is Displayed ? = ", element1)
        print("Quantity input Is Enabled ? = ", element2)

    def add_to_cart_button_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_add_to_cart_click_xpath).is_displayed()
        element2 = self.driver.find_element_by_xpath(self.product_add_to_cart_click_xpath).is_enabled()
        print("Add to cart button Is Displayed ? = ", element1)
        print("Add to cart button Is Enabled ? = ", element2)

    def like_button_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_like_click_xpath).is_displayed()
        element2 = self.driver.find_element_by_xpath(self.product_like_click_xpath).is_enabled()
        print("Like button Is Displayed ? = ", element1)
        print("Like button Is Enabled ? = ", element2)

    def details_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_details_click_xpath).is_displayed()
        print("Product Details Is Displayed ? = ", element1)

    def click_more_info(self):
        self.driver.find_element_by_xpath(self.product_more_info_click_xpath).click()

    def more_info_refer_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_more_info_refer_check_xpath).is_displayed()
        print("More Info Refers to More info ? = ", element1)

    def click_review(self):
        self.driver.find_element_by_xpath(self.product_review_click_xpath).click()

    def click_review_text(self):
        self.driver.find_element_by_xpath(self.product_review_text_click_xpath).click()

    def review_refer_check(self):
        element1 = self.driver.find_element_by_xpath(self.product_review_refer_check_xpath).is_displayed()
        print("Review Refers Reviews ? = ", element1)




