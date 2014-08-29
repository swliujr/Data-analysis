# -*- coding: UTF-8 -*-

import os,sys
from os.path import getsize
import glob
import re
import pymongo
import simplejson as json
from itertools import *
from shareres import *
from models import register
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

createtime = {'created':ctime}

#日志格式
'''
时时上传日志格式，例如：
2014-07-17 15:45:54|3109069|3.3.0|0001##jianjian_android_jianjianapp_y|GT-N7100|4.3|0E9F702F2F5AEB45D5E446B21CB64F86|1|show time|2019
'''
#客户端上传日志文件路径
dfclogbase = config.get('general','dfclogbase')
#客户端上传时时日志路径
dsclogbase = config.get('general','dsclogbase')

#连接mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
dfclogs = connection.data.dfclogs


# registerdata = Register()
# dfclogs.insert(dict(registerdata.dsclogrun(),**createtime))

logindata = Login()
dfclogs.insert(dict(registerdata.dsclogrun(),**createtime))