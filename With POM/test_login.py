from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPage
import pytest
from selenium.webdriver.chrome.options import Options


def test_successful_login():
    # Setup
    chrome_options = Options()
    chrome_options.add_extension("C:/Users/Admin/Downloads/Ublock.crx")
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Steps (Langkah-langkah yang Anda buat sebelumnya)
    login_page.open_page("https://automationexercise.com/")
    login_page.login("yusril123@example.com", "Password123")

    # Assertion (Verifikasi apakah berhasil)
    # Anda bisa menambahkan pengecekan apakah tombol "Logout" muncul
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    # Teardown
    driver.quit()