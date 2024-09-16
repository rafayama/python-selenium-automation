from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_TEXT = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_empty(self):
        self.driver.find_element(*self.EMPTY_CART_TEXT)
