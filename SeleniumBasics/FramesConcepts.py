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

class Framesconcepts():

    def framesImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/frame.xhtml")
        actualbrowser.maximize_window()
        #time.sleep(5)
        #actualbrowser.find_element(by=By.XPATH,value="//*[@id='Click' and contains(@style,'fe875d')]").click()

        """totalTags = actualbrowser.find_elements(by=By.TAG_NAME,value="iframe")
        for eachvalue in range(0,len(totalTags)):
            actualbrowser.switch_to.frame(eachvalue)
            elementExist = actualbrowser.find_elements(by=By.XPATH, value="//*[@id='Click' and contains(@style,'fe875d')]")
            if len(elementExist)>0:
                actualbrowser.find_element(by=By.XPATH, value="//*[@id='Click' and contains(@style,'fe875d')]").click()
                break"""

        time.sleep(2)

        totalTags_new = actualbrowser.find_elements(by=By.TAG_NAME, value="iframe")
        for eachvalue in range(0, len(totalTags_new)):
            innerFrameCount = actualbrowser.find_elements(by=By.TAG_NAME, value="iframe")
            if(len(innerFrameCount)>0):
                actualbrowser.switch_to.frame(eachvalue)
                totalTags_new1 = actualbrowser.find_elements(by=By.TAG_NAME, value="iframe")
                if(len(totalTags_new1)>0):
                    actualbrowser.switch_to.frame("frame2")
                    elementExist = actualbrowser.find_elements(by=By.XPATH,
                                                       value="//*[@id='Click' and contains(@style,'8e70ee')]")
                    if len(elementExist) > 0:
                        actualbrowser.find_element(by=By.XPATH, value="//*[@id='Click' and contains(@style,'8e70ee ')]").click()
                        return
                actualbrowser.switch_to.default_content()
        time.sleep(5)
obj = Framesconcepts()
obj.framesImplementation("Chrome")