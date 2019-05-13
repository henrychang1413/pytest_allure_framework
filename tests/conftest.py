# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# ******************************************
import pytest
import os
import sys
from  src.globalparam import *
from src.brower_engine import BrowserEngine
import logging

log = logging.getLogger(__name__)

@pytest.fixture(scope="class", params=["chrome"])
def web_init(request):
    log.info("class setup ==> open browser ")
    if request.param == "chrome":
        browse = BrowserEngine('Chrome')
    if request.param == "firefox":
        browse = BrowserEngine('Firefox')
    driver = browse.open_browser()
    request.cls.driver = driver
    yield BrowserEngine(request.param)
    log.info("class teardown ==> close browser")
    driver.quit()


class MyTester():
    def __init__(self, arg = ["var0", "var1"]):
        self.arg = arg
        # self.use_arg_to_init_logging_part()

    def dothis(self):
        log.info("parameters %s" %self.arg)
        log.info("this")

    def dothat(self):
        log.info("parameters %s" %self.arg)
        log.info("that")


@pytest.fixture(scope="class", params=["chrome", "firefox"])
def tester(request):
    """Create tester object"""
    return MyTester(request.param)


