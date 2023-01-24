import logging
import pytest

from data import SIDE_BAR_BUTTONS_CASES

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize('button,check_item,expected_text', SIDE_BAR_BUTTONS_CASES)
def test_side_bar_buttons(user_login, button, check_item, expected_text):
    LOGGER.debug(f"Getting method to interact with side bar element: {button}")
    press_element = getattr(user_login, button)  # get method of main page object to press sidebar button
    press_element()  # we take the name of the method to interact with the object from the list and then call it
    LOGGER.debug(f"{button} called")
    result = user_login.find_element(check_item).text == expected_text
    user_login.driver.back()  # it is important to return from the page, so the next test won't fail
    assert result
