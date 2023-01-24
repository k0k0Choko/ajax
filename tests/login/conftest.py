import logging
import pytest
from selenium.common.exceptions import NoSuchElementException

from framework.login_page import LoginPage
from framework.main_page import MainPage
from framework.start_page import StartPage
from data import LOGIN, PASSWORD

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def login_page(driver):
    """
    Navigate from the starting page to page with login form
    and return object to work with it
    """
    LOGGER.info("Navigating to login page")
    StartPage(driver).login()
    yield LoginPage(driver)


@pytest.fixture(scope='session')
def user_login(login_page):
    """
    Fixture attempts to log in if no tests were executed before.
    If log in form is not founded than user is already signed in and no actions required.
    """
    try:
        LOGGER.info("Trying to log in")
        login_page.login(LOGIN, PASSWORD)
    except NoSuchElementException:
        LOGGER.debug("User already logged in")
        pass
    finally:
        LOGGER.info("Navigating to application main page")
        yield MainPage(login_page.driver)
