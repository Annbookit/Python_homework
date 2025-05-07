from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from AuthPage import AuthPage
from ListPage import ListPage
from CartPage import CartPage
from YIPage import YIPage

def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    auth_page = AuthPage(browser)
    auth_page.auth("standard_user", "secret_sauce")
    
    list_page = ListPage(browser)
    list_page.list()

    cart_page = CartPage(browser)
    cart_page.cart()

    inforn_page = YIPage(browser)
    inforn_page.inform("Анна", "Иванова", "640000")
    itg = inforn_page.total()

    assert itg == "$58.29"

    browser.quit()
  