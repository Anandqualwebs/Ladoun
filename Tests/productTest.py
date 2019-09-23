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
from Pages.productPage import ProductPage
from Pages.checkoutPage import CheckoutPage

class ProductTest(unittest.TestCase):
    productURL = "https://ladoun.com/lm5012.html"


    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    def test__product(self):
        driver = self.driver

        self.driver.get(self.productURL)
        time.sleep(2)
        language = CheckoutPage(driver)
# English
        language.click_english()
        time.sleep(4)

        product = ProductPage(driver)
        product.main_images_visible_check()
        product.side_images_visible_check()
        product.code_avail_visible_check()
        product.quantity_input_check()
        product.add_to_cart_button_check()
        product.like_button_check()
        product.click_review()
        product.review_refer_check()
        product.details_visible_check()
        product.click_more_info()
        product.more_info_refer_check()
        product.click_review_text()
        product.review_refer_check()


    @classmethod
    def tearDownClass(inst):
     time.sleep(1)
     inst.driver.quit()
