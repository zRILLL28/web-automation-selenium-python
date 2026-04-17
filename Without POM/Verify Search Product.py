from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Buka Website
driver.get("https://automationexercise.com/")

# 2. Klik Products
driver.find_element(By.PARTIAL_LINK_TEXT, "Products").click()
#driver.find_element(By.XPATH, "//a[@href='/products']").click()

# 3. Input data
driver.find_element(By.NAME, "search").send_keys("White")
driver.find_element(By.ID, "submit_search").click()

time.sleep(3)
driver.quit()
