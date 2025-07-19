import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ListConceptsMakeMyTrip:

    def list_implementation(self,browser,expected_countrycode):
        if browser == "Chrome":
            actual_browser = webdriver.Chrome(
                service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            actual_browser = webdriver.Edge(
                service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))

        actual_browser.get("https://www.makemytrip.com/")
        actual_browser.maximize_window()
        WebDriverWait(actual_browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        actual_browser.find_element(by=By.XPATH,value="//*[@data-cy='closeModal']").click()
        WebDriverWait(actual_browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        actual_browser.find_element(by=By.XPATH,value="//*[@for='fromCity']").click()
        WebDriverWait(actual_browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-autowhatever-1']//li[1]")))

        all_cities = actual_browser.find_elements(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li")

        for each_Cities in range(1,len(all_cities)+1):

            actual_countryCode =actual_browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li["+str(each_Cities)+"]//div[starts-with(@class,'font14')]").text
            #print(actual_countryCode)
            if expected_countrycode == actual_countryCode:
                #print(actual_countryCode)
                actual_browser.find_element(by=By.XPATH,
                                            value="//*[@id='react-autowhatever-1']//li[" + str(each_Cities) + "]").click()
                break

        time.sleep(5)

obj= ListConceptsMakeMyTrip()
obj.list_implementation("Chrome","HYD")

