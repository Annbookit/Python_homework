from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireFoxSV
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FireFoxSV(GeckoDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")

search_locator = "input"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Sky")
sleep(5)
search_input.clear()

search_input.send_keys("Pro")


sleep(5)

driver.quit()
