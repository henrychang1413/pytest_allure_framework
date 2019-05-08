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


def get_mysql_server_config():
    dbconfig = {}
    dbconfig['host'] = readcf.getVal("mysql", "host")
    dbconfig['user'] = readcf.getVal("mysql", "user")
    dbconfig['passwd'] = readcf.getVal("mysql", "passwd")
    dbconfig['db'] = readcf.getVal("mysql", "db")
    dbconfig['port'] = int(readcf.getVal("mysql", "port"))
    log.info("MySQL server info: %s " % str(dbconfig))
    return dbconfig

@pytest.fixture(scope="function")
def MysqlConnect():
    log.info("\nFUNCTION SETUP ==> connect Mysql server \n")
    dbconfig = get_mysql_server_config()
    mydb = MyDB(dbconfig)
    mydb.sqlconnect()
    yield mydb
    log.info("\nFUNCTION TEARDOWN ==> disconnect Mysql server\n")
    mydb.close()

@pytest.fixture(scope="class")
def dbConnect(request):
    log.info("class setup -> connect Mysql server")

    dbconfig = get_mysql_server_config()
    db = MyDB(dbconfig)
    db.sqlconnect()
    request.cls.db = db
    yield
    log.info("class teardown -> disconnect Mysql server")
    db.close()


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    #setup part
    log.info('\n MODULE SETUP => Fetching data from db ======\n')
    yield
    #teardown part
    log.info('\n MODULE TEARDOWN => test finished ======\n')

