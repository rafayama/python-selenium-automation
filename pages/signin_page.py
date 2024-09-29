from selenium.webdriver.common.by import By

from pages.base_page import Page

class SigninPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1//span[text()='Sign into your Target account']")
    SIGNIN_FORM = (By.XPATH, "//form")
    SIGNIN_EMAIL_FIELD = (By.ID, "username")
    SIGNIN_EMAIL = 'test@test.com'
    SIGNIN_WRONG_EMAIL = 'test1@test.com'
    SIGNIN_PASSWORD_FIELD = (By.ID, "password")
    SIGNIN_PASSWORD = 'password'
    SIGNIN_WRONG_PASSWORD = 'password1'
    SIGNIN_FORM_BUTTON = (By.ID, "login")
    SIGNIN_ALERT = (By.XPATH, "//div[data-test='authAlertDisplay']")

    def verify_signin_form(self, ):
        self.verify_text(
            'Sign into your Target account',
                         *self.SIGNIN_HEADER)

    def input_email_password(self):
        self.input_text(*self.SIGNIN_EMAIL, *self.SIGNIN_EMAIL_FIELD)
        self.input_text(*self.SIGNIN_PASSWORD, *self.SIGNIN_PASSWORD_FIELD)

    def input_wrong_email_password(self):
        self.input_text(*self.SIGNIN_WRONG_EMAIL, *self.SIGNIN_EMAIL_FIELD)
        self.input_text(*self.SIGNIN_WRONG_PASSWORD, *self.SIGNIN_PASSWORD_FIELD)

    def click_signin_with_password(self):
        self.click(self.SIGNIN_FORM_BUTTON)

    def verify_user_logged_in(self):
        self.verify_text('wait_for_element_to_not_load',
                         *self.SIGNIN_HEADER)

    def verify_user_not_logged_in(self):
        self.find_element(*self.SIGNIN_ALERT)