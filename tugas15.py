
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "standard_user"
password = "secret_sauce"

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Sukses Login
    def test_login(self):
        browser = self.driver
        browser.get("https://www.saucedemo.com/")
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys(user)
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys(password)
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        responseData = browser.current_url
        self.assertIn(responseData, "https://www.saucedemo.com/inventory.html")

    # Gagal Login: Salah username
    def test_salah_username(self):
        browser = self.driver
        browser.get("https://www.saucedemo.com/")
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys(password)
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        responseData = browser.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn(responseData, "Epic sadface: Username and password do not match any user in this service")

    # Gagal Login: Salah password
    def test_salah_password(self):
        browser = self.driver
        browser.get("https://www.saucedemo.com/")
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys(user)
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("password")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        responseData = browser.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn(responseData, "Epic sadface: Username and password do not match any user in this service")
        
    # Tambah ke keranjang
    def test_tambah_ke_keranjang(self):
        browser = self.driver
        browser.get("https://www.saucedemo.com/")
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys(user)
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys(password)
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        cartValue = 0
        if(browser.find_element(By.CLASS_NAME, "shopping_cart_link").text != ""):
            cartValue = int(browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text)

        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)

        responseData = browser.find_element(By.ID, "remove-sauce-labs-backpack").text
        responseData2 = browser.find_element(By.ID, "remove-sauce-labs-bike-light").text
        responseData3 = browser.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").text
        responseDataBadge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertIn(responseData, "REMOVE")
        self.assertIn(responseData2, "REMOVE")
        self.assertIn(responseData3, "REMOVE")
        self.assertTrue(int(responseDataBadge) > cartValue)

    # Hapus dari keranjang
    def test_hapus_dari_keranjang(self):
        browser = self.driver
        browser.get("https://www.saucedemo.com/")
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys(user)
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys(password)
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        cartValue = 0
        if(browser.find_element(By.CLASS_NAME, "shopping_cart_link").text != ""):
            cartValue = int(browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text)

        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cartValue += 1
        time.sleep(1)
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        cartValue += 1
        time.sleep(1)
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        cartValue += 1
        time.sleep(2)

        browser.find_element(By.ID, "remove-sauce-labs-backpack").click()
        cartValue -= 1
        time.sleep(2)

        responseData = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text
        responseDataBadge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertIn(responseData, "ADD TO CART")
        self.assertTrue(int(responseDataBadge) == cartValue)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()