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

class Alertsconcepts():

    def AlertsImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/alert.xhtml")
        actualbrowser.maximize_window()

        actualbrowser.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        actualbrowser.switch_to.alert.accept()
        time.sleep(3)
        output = actualbrowser.find_element(by=By.ID,value="simple_result").text

        actualbrowser.find_element(by=By.ID,value="j_idt88:j_idt93").click()
        actualbrowser.switch_to.alert.dismiss()
        time.sleep(3)
        print(actualbrowser.find_element(by=By.ID, value="result").text)

        actualbrowser.find_element(by=By.ID, value="j_idt88:j_idt104").click()
        actualbrowser.switch_to.alert.send_keys("Fita Annanagar")
        print(actualbrowser.switch_to.alert.text)
        actualbrowser.switch_to.alert.accept()
        time.sleep(3)
        print(actualbrowser.find_element(by=By.ID, value="confirm_result").text)

        actualbrowser.find_element(by=By.ID,value="j_idt88:j_idt106").click()
        time.sleep(2)
        actualbrowser.find_element(by=By.ID,value="j_idt88:j_idt108").click()



obj= Alertsconcepts()
obj.AlertsImplementation("Chrome")
