from selenium import webdriver
from selenium.webdriver.common.by import By

from login_page import LoginPage
import pytest

def test_successful_login():
    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_page = LoginPage(driver)

    # Steps (Langkah-langkah yang Anda buat sebelumnya)
    login_page.open_page("https://automationexercise.com/")
    login_page.login("yusril123@example.com", "Password123")

    # Assertion (Verifikasi apakah berhasil)
    # Anda bisa menambahkan pengecekan apakah tombol "Logout" muncul
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    # Teardown
    driver.quit()