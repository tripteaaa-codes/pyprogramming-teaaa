from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_forms.asp")

time.sleep(2)

driver.find_element(By.NAME,"name").send_keys("Tripti")
driver.find_element(By.NAME,"email").send_keys("tripti@gamil.com")
driver.find_element(By.NAME,"phone").send_keys("1234567890")
driver.find_element(By.NAME,"XPATH"), "//button[@type='submit']".click()

