import pytest
from selenium.common.exceptions import NoSuchElementException

from framework.login_page import LoginPage
from framework.main_page import MainPage
from framework.start_page import StartPage
from data import LOGIN, PASSWORD


@pytest.fixture(scope='session')
def login_page(driver):
    StartPage(driver).login()
    yield LoginPage(driver)


@pytest.fixture(scope='session')
def user_login(login_page):
    try:
        login_page.login(LOGIN, PASSWORD)
    except NoSuchElementException:
        pass
    finally:
        yield MainPage(login_page.driver)
