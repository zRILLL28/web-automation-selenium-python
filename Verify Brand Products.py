from selenium import webdriver
from selenium.webdriver.common.by import By
from test_login import LoginPage
import time
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
    #assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    driver.find_element(By.PARTIAL_LINK_TEXT, "MADAME").click()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "BABYHUG").click()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "BIBA").click()

    time.sleep(3)
    driver.quit()
