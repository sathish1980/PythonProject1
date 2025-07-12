import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class Locator():

    def launch(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://www.facebook.com/")
        actualbrowser.maximize_window()
        """
        locators:
        id - By.Id
        classname
        name
        linktext
        partiallinktext
        Css
        """
        # Webelement +action = test steps

        actualbrowser.find_element(by=By.ID,value="email").send_keys("Sathish Kumar.R")
        actualbrowser.find_element(by=By.NAME, value="email").clear()
        #actualbrowser.find_element(by=By.CLASS_NAME,value="inputtext_55r1_6luy").send_keys("FITA")
        #actualbrowser.find_element(by=By.LINK_TEXT,value="Create new account").click()
        #actualbrowser.find_element(by=By.PARTIAL_LINK_TEXT, value="new").click()
        actualbrowser.find_element(by=By.CSS_SELECTOR,value="input#pass").send_keys("Passqword")
        #actualbrowser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy _9npi").send_keys("Passqword")
        actualbrowser.find_element(by=By.CSS_SELECTOR, value="input[data-testid='royal-pass']").send_keys("new")
        #actualbrowser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy _9npi[data-testid='royal-pass']").send_keys("new")
        #StartsWith - ^  input[class^='uy']
        # endsWith - $  input[class$='uy']
        # contains - *  input[class*='uy']
        # Move to next tag - > div[class="_6lux"]>input

        actualbrowser.find_element(by=By.XPATH,value="/html/body/div/div/div/div/div/div/div[2]/div/div/form/div/div/input").send_keys("test")





        time.sleep(2)



obj = Locator()
obj.launch("edge")
