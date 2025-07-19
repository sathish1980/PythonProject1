import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class ListConcepts:

    def list_concepts_implementation_static(self,browser):
        if browser == "Chrome":
            actual_browser = webdriver.Chrome(
                service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actual_browser = webdriver.Edge(
                service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actual_browser.get("https://leafground.com/select.xhtml;")
        actual_browser.maximize_window()

        actual_browser.find_element(by=By.XPATH,
                                        value="//*[@id='j_idt87:country']//*[starts-with(@class,'ui-selectonemenu-trigger')]").click()
        actual_browser.find_element(by=By.XPATH, value="//*[@id='j_idt87:country_3' and text()='India']").click()
        time.sleep(5)

obj = ListConcepts()
obj.list_concepts_implementation_static("Chrome")