import time
import unittest
import os
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from colorama import init, Fore

class accountCreationTest(unittest.TestCase):
    def setUp(self):
      init(autoreset=True)
      os.system("cls")
      warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
      self.options = webdriver.ChromeOptions()
      self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
      self.driver.maximize_window()
      
    def test(self):
      oldLabel = "Ingresar"
      driver = self.driver
      driver.get("https://tienda.centroestant.com.ar/")
      title = driver.title
      print("         "+Fore.YELLOW + "START OF TEST CASE"+"         ")
      if "Navidad - TIENDA CENTRO ESTANT" == title:
        print(Fore.CYAN+"Validate access to Centroestant: "+Fore.GREEN+"PASS")
      else:
        print(Fore.CYAN+"Validate access to Centroestant: "+Fore.RED+"FAIL")
      time.sleep(2)
      access = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").text
      if oldLabel != access:
        print(Fore.CYAN+"Validate that the 'Ingresar' item is no longer visible: "+Fore.GREEN+"PASS")
      else:
        print(Fore.CYAN+"Validate that the 'Ingresar' item is no longer visible: "+Fore.RED+"FAIL")
      driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").click()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

