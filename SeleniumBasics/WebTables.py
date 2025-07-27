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

class WebTablesconcepts():

    def WebtablesImplementation(self, browser, execpted_country):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://leafground.com/table.xhtml")
        actualbrowser.maximize_window()

        main_path = "//*[@class='ui-paginator-pages']//a"
        total_pages = actualbrowser.find_elements(by=By.XPATH,value=main_path)
        """for each_Page in total_pages:
            each_Page.click()
            time.sleep(2)"""
        for eacchrow in range(1,len(total_pages)+1):
            actualbrowser.find_element(by=By.XPATH, value=main_path+"["+str(eacchrow)+"]").click()
            time.sleep(2)
        # get total rows
            total_rows = actualbrowser.find_elements(by=By.XPATH,value="//tbody[@id='form:j_idt89_data']//tr")
            for each_row in range(1,len(total_rows)+1):
                actual_country = actualbrowser.find_element(by=By.XPATH, value="//tbody[@id='form:j_idt89_data']//tr["+str(each_row)+"]//td[2]//span[starts-with(@style,'vertical-align')]").text
                if execpted_country==actual_country:
                    representative = actualbrowser.find_element(by=By.XPATH,
                                                                value="//tbody[@id='form:j_idt89_data']//tr[" + str(
                                                                    each_row) + "]//td[3]//span[starts-with(@style,'vertical-align')]").text
                    print(representative)

        time.sleep(5)
obj = WebTablesconcepts()
obj.WebtablesImplementation("Chrome","India")