# -*- coding: UTF-8 -*-
import os
from os.path import getsize
import glob
import re
import MySQLdb as mdb
import time
import datetime
import pymongo

ctime = time.strftime('%Y-%m-%d %H:%M:%S')

#日志格式
'''
时时上传日志格式，例如：
2014-07-25 17:17:02|2014-07-27 17:17:02|3234799|3.2.4|0026##allon_android_google_y|LG-D802|4.2.2|12E1F6CA1CB85EBA11042B9C8981D5AA|0|boot
'''
dsclogformat = {
    'servertime': 0,
    'clienttime': 1,
    'userid': 2,
    'clientversion': 3,
    'channelid': 4,
    'mobilemode': 5,
    'osversion': 6,
    'deviceid': 7,
    'type': 8,
    'tag': 9
}

#客户端上传日志路径
dsclogbase = '/home/allon/python/data/constant'

#连接mongo数据库
connection=pymongo.Connection('localhost',27017)
db = connection.data
collection = db.data
dsclogs = db.dsclogs

#获取dsclog日志路径
def getdsclogpath(cd):
    lfname = '-'.join(cd) + '.log'
    cflog = dsclogbase + '/' + lfname
    return cflog

#dsclog日志数据分析
class Dsclog:
    def __init__(self,clog,cnum):
        self.clog = clog
        self.cnum = cnum
        self.fc = []
        self.fcs = []
        self.fcr = []
	self.getclumn()

    def getclumn(self):
        with open(self.clog,'r') as f:
            for line in f:
                self.fc.append(line.split('|')[self.cnum])
        self.fc.sort()
        self.fcs = set(self.fc)

    def dcresult(self):
        for i in self.fcs:
            self.fcr.append((i,self.fc.count(i)))
        return self.fcr

def getdsclogresult(date,lnum):
    date = list(date)
    cflog = getdsclogpath(date)
    rclog = Dsclog(cflog,lnum)
    return dict([str(p[0]),str(p[1])] for p in rclog.dcresult())

#dsclog中包括关键字个数
def getdsclogstag(d,k):
    r = k,getdsclogresult(d, dsclogformat[k])
    return {r[0]:r[1]}

def savedata(d,k):
    dsclogdata = getdsclogstag(d,k)
    created = {'created':ctime}
    dsclogs.insert(dict(dsclogdata,**created))

savedata(('2014','07','17'),'channelid')
