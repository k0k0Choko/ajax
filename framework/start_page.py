from .page import Page


class StartPage(Page):
    LOGIN_BTN = 'com.ajaxsystems:id/login'
    CREATE_ACC_BTN = 'com.ajaxsystems:id/registration'

    def login(self):
        self.click(StartPage.LOGIN_BTN)

    def create_account(self):
        self.click(StartPage.CREATE_ACC_BTN)
