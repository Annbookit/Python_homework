from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        """Открытие корзины"""       
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/cart.html")

    def cart(self):
        """Переход на страницу заполнение данных для доставки"""
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()