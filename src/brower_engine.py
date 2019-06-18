# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com

import os
import time
import globalparam
from selenium import webdriver
import logging

# create a logger instance
log = logging.getLogger(__name__)

class BrowserEngine(object):

    def __init__(self, browser="Chrome"):
        self.driver = None
        self.browser = browser

    def open_browser(self):
        if self.browser == "Firefox":
            self.driver = webdriver.Firefox()
            log.info("Open firefox browser.")
        elif self.browser == "Chrome":
            chrome_driver_path = globalparam.readcf.getVal("webdriver", "chromedriver")
            self.driver = webdriver.Chrome(chrome_driver_path)
            log.info("Open Chrome browser.")
        elif self.browser == "IE":
            ie_driver_path = globalparam.readcf.getVal("webdriver", "iedriver")
            self.driver = webdriver.Ie(ie_driver_path)
            log.info("Open IE browser.")
        else:
            raise NameError("Please enter a valid browser.")

        self.driver.maximize_window()
        return self.driver

    # quit browser and end testing
    def open_url(self, url=None):
        if url == None:
            #url = self.url
            url = globalparam.readcf.getVal("testServer", "URL")

        self.driver.get(url)
        log.info("Open url: %s" % url)

    def quit_browser(self):
        log.info("Quit the browser.")
        self.driver.quit()


# if __name__ == "__main__":

#     A= BrowserEngine()
#     A.open_browser()
#     A.open_url()
#     A.quit_browser()

