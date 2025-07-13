import time
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC

class syncronization():

    actualbrowser = ""

    def launch(self, browser):
        if (browser == "Chrome"):
            self.actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            self.actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        self.actualbrowser.implicitly_wait(60)
        self.actualbrowser.get("https://www.facebook.com/")
        self.actualbrowser.maximize_window()
        WebDriverWait(self.actualbrowser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Create new account']")))
        self.actualbrowser.find_element(by=By.XPATH,value="//*[text()='Create new account']").click()

        WebDriverWait(self.actualbrowser, 60).until(
            EC.visibility_of_element_located((By.NAME, "firstname")))
        self.actualbrowser.find_element(by=By.NAME,value="firstname").send_keys("Sathish")

    def CreateAccount(self):

        self.actualbrowser.implicitly_wait(60)
        self.actualbrowser.find_element(by=By.NAME, value="lastname").send_keys("kumar")
        time.sleep(10)


obj =syncronization()
obj.launch("Chrome")
obj.CreateAccount()
