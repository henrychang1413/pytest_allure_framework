# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

import time
import os
import globalparam
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import Select, WebDriverWait
import logging

# create a logger instance
log = logging.getLogger(__name__)
#logger = Logger(logger="OperatePage").getlog()

class OperatePage(object):
    """ define one page base class other page will inherit this page operations """
    def __init__(self, driver):
        self.driver = driver

    # open url on browser
    def page_open(self, url=None):
        if url == None:
            url = globalparam.readcf.getVal("testServer", "URL")
        else:
            url = url
        self.driver.get(url)
        log.info("Open url: %s" % url)

    def page_maximize(self):
        log.info("Maximize the current window.")
        self.driver.maximize_window()

    def page_wait(self, deftime=20):
        log.info("Set implicitly wait 20 seconds.")
        self.driver.implicitly_wait(20)

    # quit browser and end testing
    def page_quit(self):
        self.driver.quit()

    # forword browser
    def page_forward(self):
        self.driver.forward()
        log.info("Click forward on current page.")

    # back browser
    def page_back(self):
        self.driver.back()
        log.info("Click back on current page.")
        time.sleep(2)

    # waitting
    def page_wait(self, seconds=20):
        self.driver.implicitly_wait(seconds)
        log.info("wait for %d seconds." % seconds)

    def load_page_wait(self, tag_name, timeout=10):
        old_page = self.driver.find_element_by_tag_name(tag_name)
        log.info("wait for page loading....!")
        yield
        WebDriverWait(self.driver, timeout).until(
            EC.staleness_of(old_page)
        )
        log.info("Page is ready")

    # refresh
    def page_refresh(self):
        self.driver.refresh()
        log.info("Refresh page .")
        self.page_wait()

    # close current window
    def page_close(self):
        try:
            self.driver.close()
            log.info("Closing the browser.")
        except NameError as e:
            logger.error("Failed to close the browser with %s" % e)

    # save picture
    def get_windows_img(self):
        ctime = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())
        sname = ctime + '.png'
        screen_name = os.path.join(globalparam.img_path, sname)

        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.info("Take screenshot and save to folder: %s " % (screen_name))
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # locate element
    def find_element(self, selector):
        element = None
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        By = selector.split('=>')[0]
        value = selector.split('=>')[1]

        try:
            if By == 'id':
                element = self.driver.find_element_by_id(value)
            elif By == 'name':
                element = self.driver.find_element_by_name(value)
            elif By == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif By == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif By == 'plink':
                element = self.driver.find_element_by_partial_link_text(value)
            elif By == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif By == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            elif By == 'css':
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please enter a valid type of elements.")
                logger.error(" not find element : %s " %selector)
            log.info("Successe to find element by %s via value: %s " % ( By, value))

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()

        return element

    #for drop_box select element
    def select_child_element(self, selector):
        element = None
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        By = selector.split('=>')[0]
        val = selector.split('=>')[1]

        try:
            if By == "xpath":
                Select(self.driver.find_element_by_xpath(val))
            elif By == "id":
                Select(self.driver.find_element_by_id(val))
            elif By == "name":
                Select(self.driver.find_element_by_name(val))
            elif By == "link":
                Select(self.driver.find_element_by_link_text(val))
            elif By == "plink":
                Select(self.driver.find_element_by_partial_link_text(val))
            else:
                raise NameError("Please enter a valid type of elements.")
                logger.error(" not find element : %s " %selector)

            log.info("Successe to find element by %s via value: %s " % ( By, value))

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()

        return element


    def get_selector_text(self,selector):
        ele = self.find_element(selector)
        return ele.text

    def selector_return(self, selector, text):
        ele = self.find_element(selector)
        ele.clear()
        ele.send_keys(text)
        ele.send_keys(Keys.RETURN)

    def selector_submit(self, selector, text):
        ele = self.find_element(selector)
        ele.clear()
        ele.send_keys(text)
        ele.submit()

    # simulate keyboard to input
    def selector_input(self, selector, text):
        ele = self.find_element(selector)
        ele.clear()
        try:
            ele.send_keys(text)
            log.info("input \' %s \' " % text)
        except NameError as e:
            logger.error("Failed to input box with %s" % e)
            self.get_windows_img()

    # clear data from input box
    def selector_clear(self, selector):
        ele = self.find_element(selector)
        try:
            ele.clear()
            log.info("Clear input box before typing.")
        except NameError as e:
            logger.error("Failed to clear input box with %s" % e)
            self.get_windows_img()

    # click element
    def selector_click(self, selector):
        ele = self.find_element(selector)
        try:
            ele.click()
            log.info("The element \' %s \' was clicked." % ele.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # get title from page
    def get_page_title(self):
        log.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    def switch_alert(self):
        return self.driver.switch_to.alert()

    def switch_alert_close(self):
        self.driver.switch_to.alert().dismiss()


    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        log.info("Sleep for %d seconds" % seconds)


    # locate element
    def find_multiple_elements(self, selector):
        elements = None
        By = selector.split('=>')[0]
        value = selector.split('=>')[1]

        try:
            if By == 'id':
                elements = self.driver.find_elements_by_id(value)
            elif By == 'name':
                elements = self.driver.find_elements_by_name(value)
            elif By == 'class':
                elements = self.driver.find_elements_by_class_name(value)
            elif By == 'link':
                elements = self.driver.find_elements_by_link_text(value)
            elif By == 'plink':
                elements = self.driver.find_elements_by_partial_link_text(value)
            elif By == 'tag':
                elements = self.driver.find_elements_by_tag_name(value)
            elif By == 'xpath':
                elements = self.driver.find_elements_by_xpath(value)
            elif By == 'css':
                elements = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please enter a valid type of elements.")
                logger.error(" not find element : %s " %selector)
            log.info("Successe to find element by %s via value: %s " % ( By, value))

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()

        return elements







# class wait_page_load:
#     def __init__(self, driver=None, timeout=5):
#         self.timeout= timeout
#         self.driver = driver
#     def __enter__(self):
#         self.old_page = self.driver.find_element_by_tag_name('html')

#     def __exit__(self, *_):
#         WebDriverWait(self.driver, self.timeout).until(staleness_of(self.old_page))

    # def wait_page(self):
    #     waitpage = wait_page_load(self.driver)
    #     with waitpage:
    #         log.info("Button will click!")
    #         self.driver.find_element_by_class_name('read-more').click()
    #         log.info("Button clicked!")

    #     log.info("Page is ready")


