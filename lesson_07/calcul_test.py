from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from CalculPage import CalculPage


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    calc_page = CalculPage(browser)
    calc_page.slow_calc("45")
    calc_page.added()
    res = calc_page.result()

    assert res == 15
  
    browser.quit()
  