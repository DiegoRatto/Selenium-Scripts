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
        title = driver.title
        assert "INICIO - CENTRO ESTANT" == title, "No se ingresó a la página especificada"
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]").click()
        time.sleep(1)
        driver.find_element(By.NAME, "register").click()
        time.sleep(1)
        errorM = driver.find_element(By.XPATH, "/html/body/div[2]/ul/li/div").text
        assert errorM == messageM, f"El mensaje {messageM}, no se encontró"
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]").click()
        time.sleep(2)
        email = driver.find_element(By.ID, "reg_email")
        password = driver.find_element(By.ID, "reg_password")
        regButton = driver.find_element(By.NAME, "register")
        email.send_keys("testmail@test.com")
        password.send_keys("test")
        time.sleep(2)
        email.clear()
        password.clear()
        email.send_keys("testmail@test.com")
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

