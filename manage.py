# -*- coding: UTF-8 -*-

import os,sys
from os.path import getsize
import glob
import pymongo
import simplejson as json
from itertools import *
from models import register

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

import datetime
import time

TODAY = datetime.date.today()
ONEDAY = datetime.timedelta(days=1)
CTIME = str(TODAY - ONEDAY)
# ctime = time.strftime('%Y-%m-%d')

createtime = {'created':CTIME}

#日志格式
'''
时时上传日志格式，例如：
2014-07-17 15:45:54|3109069|3.3.0|0001##jianjian_android_jianjianapp_y|GT-N7100|4.3|0E9F702F2F5AEB45D5E446B21CB64F86|1|show time|2019
'''
# #客户端上传日志文件路径
# dfclogbase = config.get('general','dfclogbase')
# #客户端上传时时日志路径
# dsclogbase = config.get('general','dsclogbase')

#连接mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
dfclogs = connection.data.dfclogs

date = ('2014','08','24')
registerdata = register.Register(date)
dfclogs.insert(dict(registerdata.dsclogrun(),**createtime))

# logindata = Login()
# dfclogs.insert(dict(registerdata.dsclogrun(),**createtime))