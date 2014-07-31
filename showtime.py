# -*- coding: UTF-8 -*-
import os
from os.path import getsize
import glob
import re
import time
import datetime
import pymongo

'''
统计每个用户在一天中所有showtime的平均值
'''

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
ctime = time.strftime('%Y-%m-%d %H:%M:%S')

#需要统计的tag
tag = 'show time'

#定义时间字段，存储mongo记录时使用
t = {}
t['created'] = ctime

#日志格式
'''
时时上传日志格式，例如：
2014-07-17 15:45:54|3109069|3.3.0|0001##jianjian_android_jianjianapp_y|GT-N7100|4.3|0E9F702F2F5AEB45D5E446B21CB64F86|1|show time|2019
'''

#客户端上传日志文件保存路径
dfclogbase = '/home/allon/python/data/file'

#mongo数据库连接
connection=pymongo.Connection('localhost',27017)
db = connection.data
collection = db.data
showtime = db.showtime

#获取日志路径
def listfile(fd):
    str = '/'
    logpath = str.join([dfclogbase,str.join(fd),str])
    return glob.glob('%s*' % logpath)
#计算每个userid的showtime平均时间
def slog(log):
    r = {}
    v = 0
    userid = log.split('_')[1].split('.')[0]
    global reg
    reg = r'%s\|(\d+)' % tag
    imgre = re.compile(reg)
    logfile = open(log,'r')
    flog = logfile.read()
    frlog = re.findall(imgre,flog)
    logfile.close
    if frlog:
        # v = "{:.1f}".format(sum([int(x) for x in frlog])/len(frlog))
        v = sum([int(x) for x in frlog])/len(frlog)
    r[userid] = v
    return r

#计算所有userid的showtime时间
def getclogresult(date):
    date = list(date)
    getclog = listfile(date)
    userloglist = map(slog,getclog)
    return userloglist

#保存数据库
def savedata(d):
    r = {}
    r['detail'] = getclogresult(d)
    showtime.insert(dict(r,**t))

savedata(('2014','07','17'))
