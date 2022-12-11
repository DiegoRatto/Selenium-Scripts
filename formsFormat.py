import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class accountCreationTest(unittest.TestCase):
    def setUp(self):
      os.system("cls")
      self.options = webdriver.ChromeOptions()
      self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
      self.driver.maximize_window()
    
    def test(self):
        messageM = "Error: Por favor escribe una dirección de correo electrónico válida."
        messageP = "Error: Por favor, introduce la contraseña de tu cuenta."
        driver = self.driver
        driver.get("https://centroestant.com.ar/")
        time.sleep(3)
        access = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
        access.click()
        time.sleep(1)
        regButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[3]/button")
        regButton.click()
        time.sleep(1)
        errorM = driver.find_element(By.XPATH, "/html/body/div[2]/ul/li/div").text
        assert errorM == messageM, f"El mensaje {messageM}, no se encontró"
        time.sleep(2)
        access = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
        access.click()
        time.sleep(2)
        email = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[1]/input")
        password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[2]/input")
        regButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[3]/button")
        email.send_keys("asdas@pas.com")
        password.send_keys("queso")
        time.sleep(2)
        email.clear()
        password.clear()
        email.send_keys("asdaspq@mail.com")
        time.sleep(2)
        regButton.click()
        time.sleep(2)
        errorP = driver.find_element(By.XPATH, "/html/body/div[2]/ul/li/div").text
        assert errorP == messageP, f"El mensaje {messageP}, no se encontró"

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

