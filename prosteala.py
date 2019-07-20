from open_browser_handler import OpenBrowser, CloseBrowser
from time import sleep

class GoToGoogleTranslate(OpenBrowser):

    def TranslateFunction(self, message):

        self.driver.find_element_by_xpath('//input[@title="Căutați"]').send_keys("google translate", Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//div[@id="KnM9nf"]').click()
        self.driver.find_element_by_xpath('//textarea[@id="tw-source-text-ta"]').send_keys(message)
        self.driver.find_element_by_xpath('//div[@id="KnM9nf"]//span[@class="tw-menu-btn-image z1asCe JKu1je"]').click()
        sleep(10)
        self.driver.find_element_by_xpath('//div[@class="oSioSc"]//span[@class="tw-menu-btn-image z1asCe JKu1je"]').click()
        sleep(10)
        close_handler = CloseBrowser()

my_obj = GoToGoogleTranslate("https://www.google.com")
my_obj.TranslateFunction("let's go on a vacation Tatiana!")