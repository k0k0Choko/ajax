import logging
import pytest

from data import *

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize('email,pswd,expected_res', NEGATIVE_CASES)
def test_user_login_negative(login_page, email, pswd, expected_res):
    LOGGER.info(f"Trying to log in using credentials: login - {email}, password - {pswd}")
    login_page.login(email, pswd)
    assert login_page.get_snack_bar_text() == expected_res


def test_user_login_positive(login_page):
    LOGGER.info(f"Trying to log in using credentials: login - {LOGIN}, password - {PASSWORD}")
    login_page.login(LOGIN, PASSWORD)
    assert login_page.find_element('com.ajaxsystems:id/addFirstHub')
