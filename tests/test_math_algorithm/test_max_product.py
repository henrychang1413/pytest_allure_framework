# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-05-07
# ******************************************

import pytest
from src.math_calc import *
import logging
log = logging.getLogger(__name__)

def test_max_product_from_list(get_test_product_data):
    for ele in get_test_product_data:
        input_list = []
        for node in ele[0]:
            input_list.append(node)
        expected = ele[1]
        log.info(" input list  is %s, expected is %s" % (str(input_list),str(expected)) )
        calc_value = max_product_from_list(input_list)
        assert calc_value == expected, 'expected max product value is %s' %str(expected)


@pytest.mark.parametrize('input_list, expected', [([3,5,8], 40), ([2,4,-2,-5,6], 24)])
def test_max_product_from_list_parametrize(input_list,expected):
    log.info(" input list  is %s, expected is %s" % (str(input_list),str(expected)) )
    calc_value = max_product_from_list(input_list)
    assert calc_value == expected, 'expected max product value is %s' %str(expected)




if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
