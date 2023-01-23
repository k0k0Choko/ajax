import pytest

from data import SIDE_BAR_BUTTONS_CASES


@pytest.mark.parametrize('button,check_item,expected_text', SIDE_BAR_BUTTONS_CASES)
def test_side_bar_buttons(user_login, button, check_item, expected_text):
    getattr(user_login, button)()  # calling methods of main page object to press sidebar buttons
    result = user_login.find_element(check_item).text == expected_text
    user_login.driver.back()
    assert result
