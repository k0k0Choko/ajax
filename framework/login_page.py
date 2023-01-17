from .page import Page


class LoginPage(Page):
    EMAIL_FLD = 'com.ajaxsystems:id/login'
    PASSWORD_FLD = 'com.ajaxsystems:id/password'
    LOGIN_BTN = 'com.ajaxsystems:id/next'
    FORGOT_BTN = 'com.ajaxsystems:id/forgot'

    def fill_email(self, text):
        self.find_element(LoginPage.EMAIL_FLD).send_keys(text)

    def fill_password(self, text):
        self.find_element(LoginPage.PASSWORD_FLD).send_keys(text)

    def click_login(self):
        self.find_element(LoginPage.LOGIN_BTN).click()
