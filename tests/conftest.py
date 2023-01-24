import logging
import subprocess
import time

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def run_appium_server():
    """
    Starts Appium server on local host on port 4723
    """
    LOGGER.info("Server starts")
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    """
    Establishes connection with appium server
    """
    LOGGER.info("Establishing connection")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    LOGGER.info("Connection established")
    driver.implicitly_wait(10)
    yield driver
    LOGGER.info("Connection closes")
    driver.quit()
