from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Buka Website
driver.get("https://automationexercise.com/")

driver.find_element(By.LINK_TEXT, "View Product").click()
driver.find_element(By.ID, "name").send_keys("test1")
driver.find_element(By.ID, "email").send_keys("yusril123@example.com")
driver.find_element(By.ID, "review").send_keys("testtt")
driver.find_element(By.ID, "button-review").click()

time.sleep(3)
driver.quit()
