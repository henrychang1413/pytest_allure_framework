# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# ******************************************
import pytest
import os
import sys
from  src.globalparam import *
from src.mysql_connect import MyDB
import logging
log = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def get_test_product_data():
    log.info("return test data %s " % (str([((1,2,3),6), ((-1,-2,-3),6),
                                           ((-1,2,1),2), ((-3,2,8),24)])))
    return [((1,2,3),6), ((-1,-2,-3),6),((-1,2,1),2), ((-3,2,8),24)]

@pytest.fixture(scope='module')
def get_test_sum_data():
    log.info("return test data %s " % (str([((1,2,3),5), ((-1,-2,-3),-3),
                                           ((-1,2,1),3), ((-3,2,8),10)])))
    return [((1,2,3),5), ((-1,-2,-3),-3), ((-1,2,1),3), ((-3,2,8),10)]


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    #setup part
    log.info('\n MODULE SETUP => Fetching data from db ======\n')
    yield
    #teardown part
    log.info('\n MODULE TEARDOWN => test finished ======\n')

