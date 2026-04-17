# web-automation-selenium-python
Automated functional testing for E-commerce web applications using Selenium Python. Covers end-to-end scenarios from registration to checkout

Project ini merupakan kumpulan script otomatisasi pengujian (Automation Testing) untuk website E-Commerce menggunakan **Python** dan **Selenium**. Project ini fokus pada pengujian alur fungsionalitas utama (Critical Path) untuk memastikan aplikasi berjalan dengan baik.

## 🚀 Fitur yang Diuji
Script ini mencakup berbagai skenario pengujian, antara lain:
* **Autentikasi:** Registrasi akun baru, login (email benar/salah), dan logout.
* **Manajemen Produk:** Pencarian produk, melihat detail produk, serta verifikasi produk berdasarkan kategori dan brand.
* **Transaksi & Interaksi:** Menambah produk ke keranjang, menghapus produk dari keranjang, dan mengirim formulir kontak.

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Library:** Selenium WebDriver
* **Browser:** Chrome/Edge (sesuai driver yang digunakan)

## 📁 Struktur File
* `Register.py`: Menguji alur pendaftaran user baru.
* `Login with correct email & password.py`: Menguji akses masuk dengan kredensial valid.
* `Add Product in Cart.py`: Menguji fungsionalitas keranjang belanja.
* `Verify Search Product.py`: Menguji fitur pencarian barang.
* Dll

## 📊 Screenshots
<details>
<summary><b>📷 Click to view Screenshots </b></summary>
<br>

<summary><b>📷 With POM  </b></summary>
<br>

### With POM Verify Login Success
![POMSuccess](Screenshots/WithPOM_Verify_Login_Success.png)

### With POM Verify Login Failed
![POMFailed](Screenshots/WithPOM_Verify_Login_Failed.png)

### With POM Verify Brand Product
![POMBrand](Screenshots/WithPOM_Verify_Brand_Product.png)

<details>
<summary><b>📷 Without POM </b></summary>
<br>
   
### Without POM Verify Login Success
![Success](Screenshots/WithoutPOM_Verify_Login_Success.png)

### Without POM Verify Login Failed
![Failed](Screenshots/WithoutPOM_Verify_Login_Failed.png)

### Without POM Verify Form Contact Us
![POMContact](Screenshots/WithPOM_Verify_Form_Contact_Us.png)

</details>

## 📈 Pengembangan Selanjutnya (Roadmap)
Project ini adalah versi awal (Milestone 1). Rencana pengembangan berikutnya:
- [ ] Implementasi **Page Object Model (POM)** untuk efisiensi kode.
- [ ] Integrasi dengan **Pytest** sebagai framework testing.
- [ ] Pembuatan laporan pengujian otomatis menggunakan **Allure Report**.

---
*Dibuat untuk tujuan pembelajaran dan pengembangan portofolio QA.*
