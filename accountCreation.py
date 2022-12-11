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
      mailSend = "p123zas@1232.com"
      passSend = "pruebaprueba@22@"
      driver = self.driver
      driver.get("https://tienda.centroestant.com.ar/")
      time.sleep(3)
      textAccess = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").text
      assert textAccess == "Acceder", "El <span> no posee el texto ACCEDER"
      access = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
      access.click()
      time.sleep(1)
      email = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[1]/input")
      password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[2]/input")
      regButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/form/p[3]/button")
      email.send_keys(mailSend)
      password.send_keys(passSend)
      time.sleep(2)
      regButton.click()
      time.sleep(4)
      myAccount = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]")
      myAccount.click()
      time.sleep(2)
      welcomeM = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/p[1]/strong[1]").text
      assert welcomeM == mailSend[0:7], f"El nombre {mailSend[0:7]} no es visible en el mensaje de bienvenida"
    
    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


