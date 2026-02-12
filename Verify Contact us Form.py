from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Buka Website
driver.get("https://automationexercise.com/")

# 2. Klik Signup / Login
driver.find_element(By.LINK_TEXT, "Contact us").click()

# 3. Input Data
driver.find_element(By.NAME, "name").send_keys("yusril")
driver.find_element(By.NAME, "email").send_keys("yusril123@example.com")
driver.find_element(By.NAME, "subject").send_keys("test")
driver.find_element(By.NAME, "message").send_keys("test")
driver.find_element(By.NAME, "submit").click()

time.sleep(2)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

driver.find_element(By.LINK_TEXT, "Home").click()

time.sleep(3)
driver.quit()
