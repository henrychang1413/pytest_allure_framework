# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

import pytest
import logging
import time
# from src.brower_engine import BrowserEngine
from src.brower_operate import OperatePage


log = logging.getLogger(__name__)
url = "https://www.google.ca"

@pytest.mark.parametrize('web_init', ['chrome'], indirect=True)
class TestGoogleSearch():

    def test1_search_gggg(self, web_init):
        log.info('\n=== start to test case: test1_search_gggg ===\n')
        driver = self.driver
        #open base page
        homepage = OperatePage(driver)
        homepage.page_open(url)
        homepage.page_refresh()

        page_tile = homepage.get_page_title()
        log.info(page_tile)
        assert "Google" in page_tile

        search_box = "name=>q"
        input_txt = 'gggggg'
        homepage.selector_submit(search_box, input_txt)
        time.sleep(3)

        page_tile = homepage.get_page_title()
        log.info(page_tile)
        assert "gggggg" in page_tile
        homepage.get_windows_img()


    def test2_search_python(self, web_init):
        log.info('\n=== start to test case: test2_search_python ===\n')
        driver = self.driver
        #open base page
        homepage = OperatePage(driver)
        homepage.page_open(url)
        homepage.page_refresh()

        page_tile = homepage.get_page_title()
        log.info(page_tile)
        assert "Google" in page_tile

        search_box = "name=>q"
        input_txt = 'python'
        homepage.selector_submit(search_box, input_txt)
        time.sleep(2)

        page_tile = homepage.get_page_title()
        log.info(page_tile)
        assert "python" in page_tile
        homepage.get_windows_img()


if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
