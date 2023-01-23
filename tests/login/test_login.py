import pytest

from data import *


@pytest.mark.parametrize('email,pswd,expected_res', NEGATIVE_CASES)
def test_user_login_negative(login_page, email, pswd, expected_res):
    login_page.login(email, pswd)
    assert login_page.get_snack_bar_text() == expected_res


def test_user_login_positive(login_page):
    login_page.login(LOGIN, PASSWORD)
    assert login_page.find_element('com.ajaxsystems:id/addFirstHub')
