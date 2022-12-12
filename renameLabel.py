import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class accountCreationTest(unittest.TestCase):
    def setUp(self):
      os.system("cls")
      self.options = webdriver.ChromeOptions()
      self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
      self.driver.maximize_window()
      
    def test(self):
      oldLabel = "Ingresar"
      driver = self.driver
      driver.get("https://tienda.centroestant.com.ar/")
      time.sleep(2)
      access = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").text
      assert oldLabel != access, "Se encontró el item Ingresar, en el header"
      driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").click()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

