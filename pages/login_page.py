from selenium.webdriver.common.by import By

from pages.base_page import Page

class LoginPage(Page):
    TC_LINK = (By.XPATH, "//a[text()='terms and conditions']")

    def open_login_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&actions=create_session_create_account')

    def click_tc_link(self):
        self.wait_to_be_clickable_click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')
