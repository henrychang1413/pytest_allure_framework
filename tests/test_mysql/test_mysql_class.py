# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# ******************************************
import pytest
import logging
log = logging.getLogger(__name__)

@pytest.mark.usefixtures('dbConnect')
class TestJsonData():

    def test_create_table_events(self):
        log.info("===> test case: test_create_table_events ")
        mydb = self.db
        #delete table `events` if exists
        mydb.drop_table('events')
        sql = """CREATE TABLE events(
                id INT auto_increment primary key,
                event_name VARCHAR(100),
                visitor VARCHAR(100),
                properties json,
                browser json)"""
        mydb.execute(sql)

    def test_create_insert_data_to_events(self):
        log.info("===> test case: test_create_insert_data_to_events ")
        mydb = self.db

        #insert json data
        sql = """ INSERT INTO events(event_name, visitor,properties, browser)
             VALUES (
                    'pageview',
                       '1',
                       '{ "page": "/" }',
                       '{ "name": "Safari", "os": "Mac", "resolution": { "x": 1920, "y": 1080 } }'
                    ),
                    ('pageview',
                      '2',
                      '{ "page": "/contact" }',
                      '{ "name": "Firefox", "os": "Windows", "resolution": { "x": 2560, "y": 1600 } }'
                    ),
                    (
                      'pageview',
                      '1',
                      '{ "page": "/products" }',
                      '{ "name": "Safari", "os": "Mac", "resolution": { "x": 1920, "y": 1080 } }'
                    ),
                    (
                      'purchase',
                       '3',
                      '{ "amount": 200 }',
                      '{ "name": "Firefox", "os": "Windows", "resolution": { "x": 1600, "y": 900 } }'
                    )"""
        mydb.insert(sql)

        #qurery data
        sql = "select id, browser->'$.os' browser from events"
        #mydb.query(sql)
        mydb.execute(sql)
        result = mydb.fetch_all()

    def test_check_table_events_exists(self):
        log.info("===> test case: test_check_table_events_exists ")
        check_status = False
        mydb = self.db
        mydb.execute('show tables')
        result = mydb.get_fetch_list()
        log.info(result)
        for ele in result:
            if 'events' == ele.lower():
                check_status = True
        assert check_status, "table 'events' in the table list"

    def test_check_delete_events_data(self):
        log.info("===> test case: test_check_delete_events_data ")
        check_status = False
        mydb = self.db
        #qurery data
        sql = "select id, browser->'$.os' browser from events"
        #mydb.query(sql)
        mydb.execute(sql)
        result = mydb.fetch_all()
        log.info(result)
        assert len(result) == 4, " there 4 pieces of data in the table 'events' "

        # delete data where use Safari browser
        sql = "delete from events where browser->>'$.name'='Safari'"
        mydb.execute(sql)

        #query data to make sure no Safari browser.
        sql = "select browser->>'$.name' from events where browser->>'$.name'='Safari'"
        mydb.execute(sql)
        result = mydb.fetch_all()
        log.info(result)
        assert len(result) == 0 , " there are no Safari data in the table 'events' "


    def test_mysql_truncate_all_data_events(self):
        log.info("===> test case: test_mysql_truncate_all_data_events ")
        mydb = self.db

        #delete all data from events
        sql = "truncate table events"
        mydb.execute(sql)

        #check no data in the table events
        sql = "select * from events"
        mydb.execute(sql)
        result = mydb.fetch_all()
        log.info(result)
        assert len(result) == 0 , " there are no pieces of data in the table 'events' "

    def test_mysql_drop_table_events(self):
        log.info("===> test case: test_mysql_drop_table_events ")
        check_status = False
        mydb = self.db

        #delete all data
        sql = "drop table events"
        mydb.execute(sql)

        #check table employee deleted
        mydb.execute('show tables')
        result = mydb.get_fetch_list()
        log.info(result)
        for ele in result:
            if 'events' == ele.lower():
                check_status = True
        assert not check_status, "table 'events' not in the table list"


if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
