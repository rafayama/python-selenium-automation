from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCart']")
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='cartItem']")

    def verify_empty(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_TEXT)

    # METHOD 2
    # EMPTY_CART_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    #
    # def verify_empty(self):
    #     empty_text = self.driver.find_element(*self.EMPTY_CART_TEXT).text
    #     assert empty_text == 'Your cart is empty', f'Expected "Your cart is empty", but got {empty_text}'
    # METHOD 3
    # EMPTY_CART_TEXT = (By.XPATH, "//h1[text()='Your cart is empty']")
    #
    # def verify_empty(self):
    #     self.driver.find_element(*self.EMPTY_CART_TEXT)

    def add_to_cart(self):
        self.wait_to_be_clickable(*self.ADD_TO_CART_BTN)

    def open_cart_page(self):
        self.open('https://www.target.com/cart')

    def verify_cart_item(self, item):
        self.wait_for_element_to_appear(*self.CART_ITEM)