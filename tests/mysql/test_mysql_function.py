# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-05-07
# ******************************************

import pytest
import logging
log = logging.getLogger(__name__)

def test_mysql_create_table_employee(MysqlConnect):
    log.info("===> test case: test_mysql_create_table_employee ")
    mydb = MysqlConnect
    #create table
    mydb.drop_table('EMPLOYEE')
    sql = """CREATE TABLE EMPLOYEE (
         NAME  CHAR(20) NOT NULL,
         AGE INT,
         SEX CHAR(1),
         POSITION CHAR(20),
         INCOME FLOAT )"""
    mydb.execute(sql)

def test_mysql_insert_data_to_employee(MysqlConnect):
    log.info("===> test case: test_mysql_insert_data_to_employee ")
    mydb = MysqlConnect
    #insert data to table 'employee'
    sql = """INSERT INTO EMPLOYEE(NAME,AGE, SEX, INCOME)
         VALUES ('Mary', 21, 'M', 2020),
                ('Kevin', 22, 'M', 2100),
                ('David', 23, 'M', 2030),
                ('Jack', 21, 'M', 2200),
                ('Marin', 20, 'F', 2020)"""
    mydb.insert(sql)

    #query  table employee data
    sql = 'select * from EMPLOYEE'
    mydb.execute(sql)
    result = mydb.fetch_all()
    log.info(result)
    assert len(result) == 5 , " there are 5 pieces of data in the table 'EMPLOYEE' "

def test_mysql_delete_data_from_employee(MysqlConnect):
    log.info("===> test case: test_mysql_delete_data_from_employee ")
    mydb = MysqlConnect

    #delete age>21 employees not exists
    sql = "delete from EMPLOYEE where AGE > 21"
    mydb.execute(sql)

    #query age>21 employees not exists
    sql = "select * from EMPLOYEE where AGE > 21"
    mydb.execute(sql)
    result = mydb.fetch_all()
    log.info(result)
    assert len(result) == 0 , " there are no pieces of data with age>21 in the table 'EMPLOYEE' "

def test_mysql_truncate_all_data(MysqlConnect):
    log.info("===> test case: test_mysql_truncate_all_data ")
    mydb = MysqlConnect

    #delete all data
    sql = "truncate table EMPLOYEE"
    mydb.execute(sql)

    #query age>21 employees not exists
    sql = "select * from EMPLOYEE"
    mydb.execute(sql)
    result = mydb.fetch_all()
    log.info(result)
    assert len(result) == 0 , " there are no pieces of data in the table 'EMPLOYEE' "

def test_mysql_drop_table_employee(MysqlConnect):
    log.info("===> test case: test_mysql_drop_table_employee ")
    check_status = False
    mydb = MysqlConnect

    #delete all data
    sql = "drop table EMPLOYEE"
    mydb.execute(sql)

    #check table employee deleted
    mydb.execute('show tables')
    result = mydb.get_fetch_list()
    log.info(result)
    for ele in result:
        if 'employee' == ele.lower():
            check_status = True
    assert not check_status, "table 'EMPLOYEE' not in the table list"

if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )












