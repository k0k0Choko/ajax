import pytest

from framework.login_page import LoginPage
from framework.main_page import MainPage


@pytest.fixture(scope='session')
def get_to_login_page(driver):
    MainPage(driver).login()


@pytest.fixture(scope='function')
def user_login(get_to_login_page, driver):
    yield LoginPage(driver)
