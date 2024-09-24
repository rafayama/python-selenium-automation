from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    # METHOD 1
    # EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    #
    # def verify_empty(self):
    #     empty_text = self.driver.find_element(*self.EMPTY_CART_TEXT).text
    #     assert empty_text == 'Your cart is empty', f'Expected "Your cart is empty", but got {empty_text}'
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_empty(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_TEXT)

    # METHOD 3
    # EMPTY_CART_TEXT = (By.XPATH, "//h1[text()='Your cart is empty']")
    #
    # def verify_empty(self):
    #     self.driver.find_element(*self.EMPTY_CART_TEXT)