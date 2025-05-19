import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from CalculPage import CalculPage

@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Математический подсчет на калькуляторе")
@allure.description("Ввод математического дествия и получение результатов")
def test_calculator():
    with allure.step("Запуск драйвера автоматизации"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_page = CalculPage(browser)
    with allure.step("Установка времени ожидания результата"):
        calc_page.slow_calc("45")
    with allure.step("Ввод математического действия"):
        calc_page.added()
    with allure.step("Получение результата математического подсчета"):
        res = calc_page.result()    
    with allure.step("Проверка полученного и ожидаемого результатов"):
        assert res == 15
  
    browser.quit()
  