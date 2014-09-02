# -*- coding: UTF-8 -*-

import os,sys
from os.path import getsize
import pymongo
import simplejson as json
from itertools import *
from models import register,lelcs
from models.config import *
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
DSCLOGBASE = config.get('general','dsclogbase')
# #客户端上传时时日志路径
DFCLOGBASE = config.get('general','dfclogbase')

#连接mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection = pymongo.Connection(host,port)

date = ('2014','08','24')

# s_register = connection.data.s_register
# s_register.save(dict(register.dsclogrun(date,DSCLOGBASE,CHANNELLIST,REGTAGLIST),**createtime))

s_login = connection.data.s_login
s_login.save(dict(lelcs.runlelcs(date,DFCLOGBASE,LOGINTAGLIST),**createtime))
#
# s_encounter = connection.data.s_encounter
# s_encounter.save(dict(lelcs.runlelcs(date,DFCLOGBASE,ENCOUNTERTAGLIST),**createtime))
#
# s_like = connection.data.s_like
# s_like.save(dict(lelcs.runlelcs(date,DFCLOGBASE,LIKETAGLIST),**createtime))
#
# s_setting = connection.data.s_setting
# s_setting.save(dict(lelcs.runlelcs(date,DFCLOGBASE,SETINGTAGLIST),**createtime))