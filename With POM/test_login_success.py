from selenium import webdriver
from login_page import LoginPage
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_successful_login():
    # Setup
    chrome_options = Options()
    chrome_options.add_extension("C:/Users/Admin/Downloads/Ublock.crx")
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Steps (Langkah-langkah yang Anda buat sebelumnya)
    login_page.open_page("https://automationexercise.com/")
    login_page.login("yusril123@example.com", "Password123")

    # Teardown
    driver.quit()