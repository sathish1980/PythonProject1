import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC

class RadiobuttonandCheckBox():

    def checkboxImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/checkbox.xhtml")
        actualbrowser.maximize_window()
        actualbrowser.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//*[starts-with(@class,'ui-chkbox-box')]").click()
        text = actualbrowser.find_element(by=By.XPATH,
                                   value="//*[@id='j_idt87:j_idt89']//*[starts-with(@class,'ui-chkbox-box')]").get_attribute("class")
        print(text)
        time.sleep(5)
        actualbrowser.find_element(by=By.XPATH,
                                   value="//*[@id='j_idt87:j_idt89']//*[starts-with(@class,'ui-chkbox-box')]").click()

        actualbrowser.find_element(by=By.CLASS_NAME,value="ui-toggleswitch-slider").click()
        time.sleep(1)
        WebDriverWait(actualbrowser, 60).until(EC.invisibility_of_element_located((By.XPATH, "//span[@class='ui-growl-title']")))
        actualbrowser.find_element(by=By.CLASS_NAME, value="ui-toggleswitch-slider").click()
        time.sleep(2)

    def radiobuttonImplementation(self, browser,radioButton):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/radio.xhtml")
        actualbrowser.maximize_window()
        #time.sleep(2)
        actualbrowser.find_element(by=By.XPATH,value="//*[@id='j_idt87:console1']//*[text()='"+radioButton+"']//parent::td//div[starts-with(@class,'ui-radiobutton-box')]").click()
        time.sleep(2)

obj = RadiobuttonandCheckBox()
obj.checkboxImplementation("Chrome")
#obj.radiobuttonImplementation("Chrome","Edge")