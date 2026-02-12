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

# 3. Isi Name dan Email address
driver.find_element(By.NAME, "name").send_keys("Yusril")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("yusril123@example.com")

# 4. Klik tombol Signup
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

# 5. Isi form registrasi
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "password").send_keys("Password123")

Select(driver.find_element(By.ID, "days")).select_by_value("1")
Select(driver.find_element(By.ID, "months")).select_by_value("1")
Select(driver.find_element(By.ID, "years")).select_by_value("2001")

driver.find_element(By.ID, "first_name").send_keys("Yusril")
driver.find_element(By.ID, "last_name").send_keys("Arbizal")
driver.find_element(By.ID, "company").send_keys("QA Academy")
driver.find_element(By.ID, "address1").send_keys("Jl. Testing Automation No.1")
driver.find_element(By.ID, "state").send_keys("Jawa Barat")
driver.find_element(By.ID, "city").send_keys("Bandung")
driver.find_element(By.ID, "zipcode").send_keys("40211")
driver.find_element(By.ID, "mobile_number").send_keys("08123456789")

# 6. Klik Create Account
driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

# 7. Verifikasi Account Created
success_msg = driver.find_element(By.TAG_NAME, "b").text
assert success_msg == "ACCOUNT CREATED!", "❌ Gagal membuat akun!"

# 8. Klik Continue
driver.find_element(By.LINK_TEXT, "Continue").click()

time.sleep(3)
driver.quit()
