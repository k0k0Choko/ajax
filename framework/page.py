from selenium.webdriver.common.by import By


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, elem_id):
        return self.driver.find_element(By.ID, elem_id)
