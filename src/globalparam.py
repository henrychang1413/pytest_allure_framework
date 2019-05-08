# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# ******************************************

import os
import configparser
import time
import inspect

class ReadConfig:
    """
    read config file from config.ini
    """
    def __init__(self, filename):
        configpath = filename
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getVal(self, env, name):
        return self.cf.get(env,name)

current_file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Get project path
prj_path = os.path.dirname(current_file_path)
#print(prj_path)

# log path
log_path = os.path.join(prj_path, 'logs')
#print(log_path)

# report path
report_path = os.path.join(prj_path, 'report')
#print(report_path)

# test data path
data_path = os.path.join(prj_path, 'test_data')

#read config file
config_path = os.path.join(prj_path, 'config')
config_file = os.path.join(config_path, 'config.ini')
readcf = ReadConfig(config_file)




