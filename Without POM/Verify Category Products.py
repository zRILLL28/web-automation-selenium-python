from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Buka Website
driver.get("https://automationexercise.com/")

# 2. Klik Products
driver.find_element(By.LINK_TEXT, "WOMEN").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "DRESS").click()

driver.find_element(By.LINK_TEXT, "MEN").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "JEANS").click()

time.sleep(3)
driver.quit()
