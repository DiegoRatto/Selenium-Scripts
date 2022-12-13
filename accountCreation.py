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
      mailSend = ""
      passSend = ""
      driver = self.driver
      driver.get("https://tienda.centroestant.com.ar/")
      title = driver.title
      assert "INICIO - CENTRO ESTANT" == title, "No se ingresó a la página especificada"
      time.sleep(3)
      textAccess = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").text
      assert textAccess == "Acceder", "El item acceder no se encuentra en el Header"
      driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]").click()
      time.sleep(1)
      email = driver.find_element(By.ID, "reg_email")
      password = driver.find_element(By.ID, "reg_password")
      regButton = driver.find_element(By.NAME, "register")
      email.send_keys(mailSend)
      password.send_keys(passSend)
      time.sleep(2)
      regButton.click()
      time.sleep(4)
      driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]").click()
      time.sleep(2)
      welcomeM = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/p[1]/strong[1]").text
      assert welcomeM == mailSend[0:8], f"El nombre {mailSend[0:8]} no es visible en el mensaje de bienvenida"
    
    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


