from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireFoxSV
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FireFoxSV(GeckoDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

search_locator_U = "#username"
search_locator_P = "#password"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator_U)
search_input.send_keys("tomsmith")

search_input = driver.find_element(By.CSS_SELECTOR, search_locator_P)
search_input.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button").click()


text_end = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
print(text_end)

sleep(5)

driver.quit()
