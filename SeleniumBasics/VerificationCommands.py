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

class Verificationconcepts():

    def verificationimplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/dashboard.xhtml")
        actualbrowser.maximize_window()
        print(actualbrowser.title)
        print(actualbrowser.current_url)
        print(actualbrowser.current_window_handle)
        print(actualbrowser.find_element(by=By.XPATH,value="//*[@id='j_idt154_content']//tr[1]//th[1]").text)
        print(actualbrowser.find_element(by=By.XPATH,value="//*[@id='j_idt154_content']//tr[1]//th[1]").get_attribute("style"))
        print(actualbrowser.find_element(by=By.XPATH, value="//*[@id='j_idt154_content']//tr[1]//th[1]").get_property(
            "style"))
        print(actualbrowser.find_element(by=By.XPATH,value="(//*[contains(@class,'pi-angle-up')])[1]").value_of_css_property("color"))
        ##4caf50
        print(actualbrowser.find_element(by=By.XPATH,
                                         value="(//*[contains(@class,'pi-angle-up')])[1]").value_of_css_property(
            "font-size"))

obj = Verificationconcepts()
obj.verificationimplementation("Chrome")
