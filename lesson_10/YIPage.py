from selenium.webdriver.common.by import By

class YIPage:

    def __init__(self, driver):
        self._driver = driver

    def inform(self, fn: str, ln: str, pc: str):
        """Ввод данных для доставки. Переход на страницу с итоговой суммой"""
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(fn)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(ln)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(pc)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total(self):
        """Получение финальной суммы заказа"""
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        itg = total.split()[1]
        """
        Метод вернет строковое значение
        """
        return itg