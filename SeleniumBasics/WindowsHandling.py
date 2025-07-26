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

class Windowsconcepts():

    def WindowsImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/window.xhtml")
        actualbrowser.maximize_window()
        parentWindow = actualbrowser.current_window_handle # current window name
        print(parentWindow)
        actualbrowser.find_element(by=By.ID,value="j_idt88:new").click()

        allWindowsname = actualbrowser.window_handles # return all the windows name
        print(allWindowsname)
        for eachwindow in allWindowsname:
            if eachwindow!=parentWindow:
                actualbrowser.switch_to.window(eachwindow)
                elementexist = actualbrowser.find_elements(by=By.ID,value="menuform:j_idt40")
                if( len(elementexist)>0):
                    actualbrowser.find_element(by=By.ID, value="menuform:j_idt40").click()
                    actualbrowser.find_element(by=By.ID,value="menuform:m_input").click()
                    actualbrowser.find_element(by=By.ID,value="j_idt88:name").send_keys("Sathish")
                    break
        actualbrowser.switch_to.window(parentWindow)
        time.sleep(5)

obj = Windowsconcepts()
obj.WindowsImplementation("Chrome")


