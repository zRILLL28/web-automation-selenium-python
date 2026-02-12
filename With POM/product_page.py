from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Menunggu maksimal 10 detik

    def click_brand(self, brand_name):
        """Fungsi untuk klik brand dengan penanganan iklan"""
        try:
            # 1. Tunggu sampai elemen muncul dan bisa diklik
            locator = (By.PARTIAL_LINK_TEXT, brand_name)
            element = self.wait.until(EC.element_to_be_clickable(locator))

            # 2. Scroll ke elemen agar terlihat di layar
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # 3. Coba klik standar
            element.click()
        except Exception:
            # 4. Jika gagal (karena tertutup iklan), paksa klik menggunakan JavaScript
            print(f"Klik standar gagal pada {brand_name}, mencoba JavaScript Click...")
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, brand_name)
            self.driver.execute_script("arguments[0].click();", element)