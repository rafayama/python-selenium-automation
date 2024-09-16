class Page:

    def click(self):
        print('Clicking')

    def input_text(self, text):
        print(f'Entering: {text}')

    def find_element(self):
        print('Searching')

class LoginPage(Page):
    # pass
    def login(self):
        self.find_element()
        self.click()
page = Page()
page.input_text('test text')
page.click()

login_page = LoginPage()
login_page.input_text('login')