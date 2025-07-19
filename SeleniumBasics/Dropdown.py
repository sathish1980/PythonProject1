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

class Dropdown():

    def DropdownImplementation(self, browser):
        if (browser == "Chrome"):
            actualbrowser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actualbrowser = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actualbrowser.get("https://www.amazon.com/")
        actualbrowser.maximize_window()
        actualbrowser.find_element(by=By.CLASS_NAME,value="a-button-text").click()
        time.sleep(5)
        ProductList = Select(actualbrowser.find_element(by=By.ID,value="searchDropdownBox"))
        multiselectorNot = ProductList.is_multiple
        print(multiselectorNot)
        if multiselectorNot != "false":
            #ProductList.select_by_index(3)
            #ProductList.select_by_value("search-alias=beauty-intl-ship")
            ProductList.select_by_visible_text("Kindle Store")
        else:
            ProductList.deselect_by_index()
            ProductList.deselect_by_value()
            ProductList.deselect_by_visible_text()
            ProductList.deselect_all()


        time.sleep(5)

obj = Dropdown()
obj.DropdownImplementation("Chrome")


