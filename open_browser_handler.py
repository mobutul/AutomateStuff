from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class OpenBrowser():

    driver = webdriver.Firefox()

    def __init__(self, url_address):

        self.driver.get(url_address)
        sleep(2)

class CloseBrowser(OpenBrowser):

    def __init__(self):
        self.driver.close()


