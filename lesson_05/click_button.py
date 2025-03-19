from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for but in range (1, 6):
    driver.find_element(By.CSS_SELECTOR, "button").click()

dels = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

print(len(dels))

sleep(5)

driver.quit()