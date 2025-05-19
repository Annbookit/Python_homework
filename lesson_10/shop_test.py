import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from AuthPage import AuthPage
from ListPage import ListPage
from CartPage import CartPage
from YIPage import YIPage
 
@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Покупка товаров в интернет-магазине")
@allure.description("Покупка товаров и доставка. Авторизированный пользователь")
def test_shop():
    with allure.step("Запуск драйвера автоматизации"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.implicitly_wait(15)
    with allure.step("Авторизация пользователя"):
        auth_page = AuthPage(browser)
        auth_page.auth("standard_user", "secret_sauce")
    with allure.step("Добавление товаров в корзину"):    
        list_page = ListPage(browser)
        list_page.list()
    with allure.step("Открытие корзины"):
        cart_page = CartPage(browser)
        cart_page.cart()
    with allure.step("Ввод данных для доставки"):
        inforn_page = YIPage(browser)
        inforn_page.inform("Анна", "Иванова", "640000")
    itg = inforn_page.total()
    with allure.step("Сравнение ожидаемого и полученного результатов"):
        assert itg == "$58.29"

    browser.quit()
  