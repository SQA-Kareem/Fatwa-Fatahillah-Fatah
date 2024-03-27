import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, email, password):
        # Mencari elemen input email dan password menggunakan ID
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(email)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol SignIn
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(5)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

        time.sleep(2)

    def detail_magang(self):
        # Masuk halaman cari magang
        button = self.driver.find_element(By.XPATH, "//a[@href='cariInternship.html']")
        button.click()

        time.sleep(2)

        # Memilih salah satu magang
        button = self.driver.find_element(By.XPATH, "//a[@href='detailMagang?magangId=65ab797ca8b25e04a4b4b518']")
        button.click()

        time.sleep(2)

    def test_detail_magang(self):
        # Membuka halaman web
        self.driver.get("https://intermoni.my.id/") 

        time.sleep(2)

        # Tunggu hingga navbar-burger menjadi klikable
        # navbar_burger = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "navbar-burger")))
        # navbar_burger.click()

        # Masuk halaman login
        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signIn.html']")
        button.click()

        time.sleep(2)

        # Login dengan email dan password
        self.login("dimasmhs@gmail.com", "fghjkliow")

        self.detail_magang()


if __name__ == "__main__":
    unittest.main()