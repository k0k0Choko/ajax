from .page import Page


class LoginPage(Page):
    EMAIL_FLD = 'com.ajaxsystems:id/login'
    PASSWORD_FLD = 'com.ajaxsystems:id/password'
    LOGIN_BTN = 'com.ajaxsystems:id/next'
    FORGOT_BTN = 'com.ajaxsystems:id/forgot'
    SNACK_BAR = 'com.ajaxsystems:id/snackbar_text'

    def fill_email(self, text):
        email = self.find_element(LoginPage.EMAIL_FLD)
        email.clear()
        email.send_keys(text)

    def fill_password(self, text):
        pswd = self.find_element(LoginPage.PASSWORD_FLD)
        pswd.clear()
        pswd.send_keys(text)

    def click_login(self):
        self.find_element(LoginPage.LOGIN_BTN).click()

    def get_snack_bar_text(self):
        return self.find_element(LoginPage.SNACK_BAR).text
