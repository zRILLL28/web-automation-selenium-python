from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Buka Website
driver.get("https://automationexercise.com/")

# 2. Klik Products
driver.find_element(By.PARTIAL_LINK_TEXT, "View Product").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "cart").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "View Cart").click()

time.sleep(3)
driver.quit()
