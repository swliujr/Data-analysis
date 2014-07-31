# -*- coding: UTF-8 -*-
import os
from os.path import getsize
import glob
import re
import MySQLdb as mdb
import time
import datetime
import pymongo
import simplejson as json

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
ctime = time.strftime('%Y-%m-%d %H:%M:%S')

#tag列表
taglist = [
    'boot',
    'mobile phone users_register interface',
    'mobile phone verification code',
    'micro-blog import',
    'micro-blog registry access',
]

channellist = [
    '0001##allon_android_allonapp_y',
    '0002##allon_android_allon3g_y',
    '0003##allon_android_allonweb_y',
]

#日志格式
'''
时时上传日志格式，例如：
2014-07-25 17:17:02|2014-07-27 17:17:02|3234799|3.2.4|0026##allon_android_google_y|LG-D802|4.2.2|12E1F6CA1CB85EBA11042B9C8981D5AA|0|boot
'''

#客户端上传日志文件保存路径
dfclogbase = '/home/allon/python/data/file'

#mongo数据库
connection=pymongo.Connection('localhost',27017)
db = connection.data
collection = db.data
dfclogs = db.dfclogs

#获取日志路径

def getssclogresult(date,lnum):
    date = list(date)
    cflog = getdfclog(date)
    rclog = Dclog(cflog,lnum)
    return rclog.dcresult()

#分析定时上传日志
def listfile(fd):
    str = '/'
    logpath = str.join([dfclogbase,str.join(fd),str])
    return glob.glob('%s*' % logpath)

def slog(log):
    imgre = re.compile(reg)
    logfile = open(log,'r')
    flog = logfile.read()
    frlog = re.findall(imgre,flog)
    logfile.close
    return frlog

def getclogresult(date,channel):
    date = list(date)
    getclog = listfile(date)
    r = {}
    global reg
    for tag in taglist:
        reg = r'%s(.*)1\|%s' % (channel,tag)
        userloglist = filter(slog,getclog)
        useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
        r[tag] = {"userid":useridlist,"total":len(useridlist)}
    return r

def getchannelr(d):
    l = {}
    for channel in channellist:
        l[channel] = getclogresult(d,channel)
    return l


def savedata(d):
    created = {'created':ctime}
    dfclogs.insert(dict(getchannelr(d),**created))

savedata(('2014','07','17'))
