from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SIGNIN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGNIN_SIDEBAR_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(5)

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)

    def click_signin(self):
        self.wait_to_be_clickable(*self.SIGNIN_BTN)

    def click_signin_sidebar(self):
        self.wait_to_be_clickable_click(*self.SIGNIN_SIDEBAR_BTN)

