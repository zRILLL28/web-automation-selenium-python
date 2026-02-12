from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage  # Import Page Object baru
import pytest


def test_successful_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)  # Inisialisasi

    login_page.open_page("https://automationexercise.com/")
    login_page.login("yusril123@example.com", "Password123")

    product_page.click_brand("MADAME")
    product_page.click_brand("BABYHUG")
    product_page.click_brand("BIBA")

    driver.quit()