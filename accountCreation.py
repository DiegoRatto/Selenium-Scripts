import time
import unittest
import os
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
      mailSend = "test30@test2022.com"
      passSend = "Testtest2022@"
      driver = self.driver
      driver.get("https://tienda.centroestant.com.ar/")
      title = driver.title
      print("         "+Fore.YELLOW + "START OF TEST CASE"+"         ")
      if "Navidad - TIENDA CENTRO ESTANT" == title:
          print(Fore.CYAN+"Validate access to Centroestant: "+Fore.GREEN+"PASS")
      else:
          print(Fore.CYAN+"Validate access to Centroestant: "+Fore.RED+"FAIL")
      time.sleep(3)
      textAccess = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[1]/div/div[3]/ul/li[2]/a/span").text
      if textAccess == "Acceder":
        print(Fore.CYAN+"Validate the visibility of the item 'Acceder': "+Fore.GREEN+"PASS")
      else:
        print(Fore.CYAN+"Validate the visibility of the item 'Acceder': "+Fore.RED+"FAIL")
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
      if welcomeM == mailSend[0:6]:
        print(Fore.CYAN+"Validate user login: "+Fore.GREEN+"PASS")
      else:
        print(Fore.CYAN+"Validate user login: "+Fore.RED+"FAIL")
    
    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


