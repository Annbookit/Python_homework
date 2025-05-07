from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
Address = driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
Zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
City = driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
Country = driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
Email = driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
Phone_number = driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
Job_position = driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
Company = driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")

assert first_name.find("alert-succes") != -1
assert last_name.find("alert-succes") != -1
assert Address.find("alert-succes") != -1
assert Zip_code.find("alert-danger") != -1
assert City.find("alert-succes") != -1
assert Country.find("alert-succes") != -1
assert Email.find("alert-succes") != -1
assert Phone_number.find("alert-succes") != -1
assert Job_position.find("alert-succes") != -1
assert Company.find("alert-succes") != -1

sleep(5)
