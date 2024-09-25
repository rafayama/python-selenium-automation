from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SigninPage
from pages.target_app_page import TargetAppPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SigninPage(driver)
        self.target_app_page = TargetAppPage(driver)




# app = Application()
# app.header.search_product()
# app.search_results_page.verify_results()