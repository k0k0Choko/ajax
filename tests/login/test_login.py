import pytest

from data import *


@pytest.mark.parametrize('email,pswd,expected_res', negative_cases)
def test_user_login_negative(user_login, email, pswd, expected_res):
    user_login.fill_password(pswd)
    user_login.fill_email(email)
    user_login.click_login()
    assert user_login.get_snack_bar_text() == expected_res


def test_user_login_positive(user_login):
    user_login.fill_password(password)
    user_login.fill_email(login)
    user_login.click_login()
    assert user_login.find_element('com.ajaxsystems:id/addFirstHub')
