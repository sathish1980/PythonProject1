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

class Scrollconcepts():

    def scrollImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/dashboard.xhtml")
        actualbrowser.maximize_window()
        # horizontal , Vertical
        actualbrowser.execute_script("window.scrollTo(0, 600)") # scroll down
        actualbrowser.execute_script("window.scrollTo(0, -200)") # scroll up
        actualbrowser.execute_script("window.scrollTo(100, 0)") # scroll right
        actualbrowser.execute_script("window.scrollTo(-200, 0)") #scroll left

        #completly down
        actualbrowser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # completly up
        actualbrowser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        time.sleep(2)
        # completly right
        actualbrowser.execute_script("window.scrollTo(document.body.scrollHeight,0);")
        time.sleep(2)
        # completly left
        actualbrowser.execute_script("window.scrollTo(-document.body.scrollHeight,0);")
        time.sleep(2)
        #scroll to an element
        element = actualbrowser.find_element(By.ID, "j_idt154_header")
        actualbrowser.execute_script("arguments[0].scrollIntoView()", element)

        time.sleep(2)



obj = Scrollconcepts()
obj.scrollImplementation("Chrome")
