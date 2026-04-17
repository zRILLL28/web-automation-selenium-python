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
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# 3. Input data
driver.find_element(By.NAME, "email").send_keys("yusril123@example.com")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Products").click()
#driver.find_element(By.XPATH, "//a[@href='/products']").click()

driver.find_element(By.NAME, "search").send_keys("White")
driver.find_element(By.ID, "submit_search").click()

driver.find_element(By.LINK_TEXT, "Add to cart").click()

time.sleep(3)

driver.find_element(By.PARTIAL_LINK_TEXT, "View Cart").click()

time.sleep(3)
driver.quit()
