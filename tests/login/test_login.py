from credentials import *


def test_user_login(user_login):
    user_login.fill_password(password)
    user_login.fill_email(login)
    user_login.click_login()
    assert user_login.find_element('com.ajaxsystems:id/addFirstHub')
