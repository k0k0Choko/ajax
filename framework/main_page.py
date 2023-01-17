from .page import Page


class MainPage(Page):
    LOGIN_BTN = 'com.ajaxsystems:id/login'
    CREATE_ACC_BTN = 'com.ajaxsystems:id/registration'

    def login(self):
        self.find_element(MainPage.LOGIN_BTN).click()

    def create_account(self):
        self.find_element(MainPage.CREATE_ACC_BTN).click()
