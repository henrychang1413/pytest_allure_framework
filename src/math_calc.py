# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-05-07
# ******************************************

import logging
log = logging.getLogger(__name__)

#return max product of two elements in  an unordered list
def max_product_from_list(l):
    if len(l) <2:
        log.error('list length is less than 2, input error')
        raise ValueError
    b1,b2 = sorted(l, reverse=True)[0:2]
    return b1*b2

#return max sum of two elements in an unordered list
def max_sum_from_list(l):
    if len(l) <2:
        log.error('list length is less than 2, input error')
        raise ValueError
    b1,b2 = sorted(l, reverse=True)[0:2]
    return b1+b2
