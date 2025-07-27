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

class ScreenShotconcepts():

    def screenshotimplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/dashboard.xhtml")
        actualbrowser.maximize_window()
        actualbrowser.get_screenshot_as_file('C:\\Users\\DELL\\PycharmProjects\\PythonProject1\\Screenshot\\dashboard.png')
        # scroll to an element
        element = actualbrowser.find_element(By.ID, "j_idt154_header")
        actualbrowser.execute_script("arguments[0].scrollIntoView()", element)
        actualbrowser.get_screenshot_as_file(
            'C:\\Users\\DELL\\PycharmProjects\\PythonProject1\\Screenshot\\dashboard1.png')

        time.sleep(2)
obj = ScreenShotconcepts()
obj.screenshotimplementation("Chrome")