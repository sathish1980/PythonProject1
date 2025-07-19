import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC

class ListConceptsDynamic():

    """
        Step 1 : launch the browser and enter the url
        Step 2 : click on the Country list
        Step 3 : Get all the countries and store it in List
        Step 4 : Compare the actual countries vs expected countries
        Step 5 : If that matched click the respective country
    """
    actualbrowser = "null"
    def ListConceptsImplementation(self, browser, expectedCountryname):
        if (browser == "Chrome"):
            self.actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            self.actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        self.actualbrowser.get("https://leafground.com/select.xhtml;")
        self.actualbrowser.maximize_window()
        self.actualbrowser.find_element(by=By.XPATH,value="//*[@id='j_idt87:country']//*[starts-with(@class,'ui-selectonemenu-trigger')]").click()
        allCountries = self.actualbrowser.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        for eachCountry in allCountries:
            actualCountryname = eachCountry.text
            if expectedCountryname == actualCountryname:
                eachCountry.click()
                break
        time.sleep(5)

obj = ListConceptsDynamic()
obj.ListConceptsImplementation("Chrome","Brazil")