from selenium.webdriver.common.by import By

from pages.base_page import Page

class LoginPage(Page):


    def open_login_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&actions=create_session_create_account')



