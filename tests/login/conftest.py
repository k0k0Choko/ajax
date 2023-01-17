import pytest

from framework.login_page import LoginPage
from framework.main_page import MainPage


@pytest.fixture(scope='function')
def user_login(driver):
    MainPage(driver).login()
    yield LoginPage(driver)
