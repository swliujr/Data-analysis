# -*- coding: UTF-8 -*-

import pymongo
from models import config,register,lelcs,login,encounter,like,setting

import datetime

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

#连接mongo数据库

connection = pymongo.Connection(config.MQHOST,config.MQPORT)

date = ('2014','08','24')

# s_register = connection.data.s_register
# s_register.save(dict(register.dsclogrun(date,config.DSCLOGBASE,config.CHANNELLIST,config.REGTAGLIST),**createtime))

# s_login = connection.data.s_login
# s_login.save(dict(login.meregdict(date,config.DFCLOGBASE,config.LOGINTAGLIST),**createtime))

s_encounter = connection.data.s_encounter
s_encounter.save(dict(encounter.meregdict(date,config.DFCLOGBASE,config.ENCOUNTERTAGLIST),**createtime))

# s_like = connection.data.s_like
# s_like.save(dict(like.tagdata(date,config.DFCLOGBASE,config.LIKETAGLIST),**createtime))

#s_chat = connection.data.s_chat
#s_chat.save(dict(chat.rundata(),**createtime))

s_setting = connection.data.s_setting
s_setting.save(dict(setting.tagdata(date,config.DFCLOGBASE,config.SETINGTAGLIST),**createtime))
