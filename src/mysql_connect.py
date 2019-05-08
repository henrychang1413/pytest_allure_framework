# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-05-03
# ******************************************
import pymysql
import os
import time
import globalparam
import logging
log = logging.getLogger(__name__)

class MyDB:
    def __init__(self, dbconfig):
        self.host = dbconfig['host']
        self.user = dbconfig['user']
        self.password = dbconfig['passwd']
        self.db = dbconfig['db']
        self.port = dbconfig['port']
        self.cur = None
        self.conn = None

    def sqlconnect(self):
        try:
            self.conn = pymysql.connect(host = self.host,
                                        user = self.user,
                                        password = self.password,
                                        db = self.db,
                                        port = self.port)

        except Exception as e:
           log.error(e)

        self.cur =  self.conn.cursor()
        log.info("success to connect sql server: %s with username=%s password=%s "
              % (self.host, self.user, self.password))
        return self.cur

    def create_database(self, dbname):
        log.info("create database : %s" % dbname)
        sql = "drop database if exists %s" %dbname
        self.execute(sql)
        sql = 'create database %s' %dbname
        self.execute(sql)

    def drop_table(self, tabname):
        log.info("delete table : %s" % tabname)
        sql = "drop table if exists %s" %tabname
        self.execute(sql)

    def execute(self, sql):
        log.info("execute sql statement: %s" % sql)
        try:
            result= self.cur.execute(sql)
        except Exception as e:
            log.error(e)
        return result

    def fetch_all(self):
        log.info("fetch all sql result: " )
        rows = self.cur.fetchall()
        for row in rows:
            log.info(row)
        return rows

    #get fetch list, not tuple value
    def get_fetch_list(self):
        fetch_rows = self.fetch_all()
        return_list = []
        for ele in fetch_rows:
            return_list.append(ele[0])
        return return_list

    def commit(self):
        log.info("execute 'commit' operation")
        self.conn.commit()

    def rollback(self):
        log.info("execute 'rollback' operation")
        self.conn.rollback()

    def alter(self, sql):
        try:
            rows = self.cur.execute(sql)
            if rows > 0:
               self.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()


    def insert(self, sql):
        try:
            self.execute(sql)
            self.commit()
        except:
            self.rollback()

    def insert_many(self, sql):
        try:
            self.executemany(sql)
            self.commit()
        except:
            self.rollback()

    def __del__(self):
        try:
            self.cur.close()
            self.conn.close()
        except:
            pass

    def  close(self):
        log.info("disconnect sql server")
        self.__del__()


if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1', 'user':'root',
            'passwd':'123456', 'db':'test', 'port':3306}

    mydb =MyDB(dbconfig)
    # mydb.sqlconnect()
    # mydb.execute('show tables')
    # result = mydb.fetch_all()

    # #create table
    # mydb.drop_table('EMPLOYEE')
    # sql = """CREATE TABLE EMPLOYEE (
    #      NAME  CHAR(20) NOT NULL,
    #      AGE INT,
    #      SEX CHAR(1),
    #      POSITION CHAR(20),
    #      INCOME FLOAT )"""
    # mydb.execute(sql)
    # sql = """INSERT INTO EMPLOYEE(NAME,AGE, SEX, INCOME)
    #      VALUES ('John', 20, 'M', 2000)"""

    # mydb.insert(sql)
    # sql = 'select * from EMPLOYEE'
    # mydb.query(sql)

    # sql = """INSERT INTO EMPLOYEE(NAME,AGE, SEX, INCOME)
    #      VALUES ('Mary', 21, 'M', 2020),
    #             ('Kevin', 22, 'M', 2100),
    #             ('David', 23, 'M', 2030),
    #             ('Jack', 21, 'M', 2200),
    #             ('Marin', 20, 'F', 2020)"""

    # mydb.insert(sql)
    # sql = 'select * from EMPLOYEE'
    # mydb.query(sql)

    # #insert data
    # mydb.close()
