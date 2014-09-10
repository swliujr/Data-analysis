# -*- coding: UTF-8 -*-
import os,sys
from os.path import getsize
import glob
import re
import pymongo
from shareres import *
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

#客户端上传日志路径
dsclogbase = config.get('general','dsclogbase')

#连接mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
dsclogs = connection.data.dsclogs

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

    def dcresult(self):
        with open(self.clog,'r') as f:
            for line in f:
                self.fc.append(line.split('|')[self.cnum])
        self.fc.sort()
        for i in set(self.fc):
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

date = (sys.argv[1],sys.argv[2],sys.argv[3])
savedata(date,sys.argv[4])
