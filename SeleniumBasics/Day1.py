import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService


class day1():

    def launch(self,browser):
        if(browser=="Chrome"):
            driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        else:
            driver = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))
        driver.maximize_window() # Maximize
        #driver.minimize_window()
        driver.get("https://www.google.com/") # enter the url
        value = driver.current_url #retrieve
        print(value)
        #driver.quit() # close the browser
        driver.back()
        time.sleep(1)
        driver.get("https://www.facebook.com/")  #
        driver.back()
        time.sleep(1)
        driver.forward()
        driver.refresh()
        time.sleep(5)

obj = day1()
obj.launch("Edge")