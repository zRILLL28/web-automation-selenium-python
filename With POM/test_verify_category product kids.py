from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage  # Import Page Object baru
import pytest
import time
from selenium.webdriver.chrome.options import Options


def test_successful_login():
    chrome_options = Options()
    chrome_options.add_extension("C:/Users/Admin/Downloads/Ublock.crx")
    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)  # Inisialisasi

    login_page.open_page("https://automationexercise.com/")
    login_page.login("yusril123@example.com", "Password123")

    product_page.click_brand("KIDS")
    time.sleep(2)
    product_page.click_brand("DRESS")
    product_page.click_brand("KIDS")
    time.sleep(2)
    product_page.click_brand("TOPS & SHIRTS")

    driver.quit()