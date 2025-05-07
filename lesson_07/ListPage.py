from selenium.webdriver.common.by import By

class ListPage:

    def __init__(self, driver):
        self._driver = driver

    def list(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()