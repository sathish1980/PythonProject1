import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC

class Mouseconcepts():

    def MouseImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://www.ebay.com/")
        actualbrowser.maximize_window()
        mouse_actions = ActionChains(actualbrowser)
        mouse_actions.move_to_element(actualbrowser.find_element(by=By.XPATH,value="//*[@class='vl-flyout-nav__js-tab']//a[text()='Motors']")).perform()
        mouse_actions.move_to_element(actualbrowser.find_element(by=By.XPATH,value="//*[text()='Tools and supplies']")).click().perform()

        time.sleep(5)

    def MouseImplementation2(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/drag.xhtml")
        actualbrowser.maximize_window()
        mouse_actions = ActionChains(actualbrowser)
        mouse_actions.move_to_element(actualbrowser.find_element(by=By.ID,value="form:drag_content")).drag_and_drop(actualbrowser.find_element(by=By.ID,value="form:drag_content"),actualbrowser.find_element(by=By.ID,value="form:drop_content")).perform()

        mouse_actions.move_to_element(actualbrowser.find_element(by=By.ID, value="form:conpnl_content")).drag_and_drop_by_offset(actualbrowser.find_element(by=By.ID, value="form:conpnl_content"),200,0).perform()
        time.sleep(3)
        mouse_actions.move_to_element(
            actualbrowser.find_element(by=By.ID, value="form:conpnl_content")).drag_and_drop_by_offset(
            actualbrowser.find_element(by=By.ID, value="form:conpnl_content"), -60, 0).perform()

        time.sleep(5)

    def MouseImplementation3(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://www.facebook.com/")
        actualbrowser.maximize_window()
        mouse_actions = ActionChains(actualbrowser)
        mouse_actions.move_to_element(actualbrowser.find_element(by=By.ID,value="email")).send_keys("sathish").double_click().context_click().perform()
        time.sleep(5)


obj=Mouseconcepts()
obj.MouseImplementation3("Chrome")
