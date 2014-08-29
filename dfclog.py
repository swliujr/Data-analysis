# -*- coding: UTF-8 -*-
import os,sys
from os.path import getsize
import glob
import re
import pymongo
import simplejson as json
from itertools import *
from shareres import *
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

#分析定时上传日志获取各个tag数量
def getssclogresult(date,lnum):
    date = list(date)
    cflog = getdfclog(date)
    rclog = Dclog(cflog,lnum)
    return rclog.dcresult()

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
    for tag in dftaglist:
        reg = r'%s(.*)1\|%s' % (channel,tag)
        userloglist = filter(slog,getclog)
        useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
        r[tag] = {"userid":useridlist,"total":len(useridlist)}
    return r

def rundfdata(d):
    l = {}
    for channel in channellist:
        l[channel] = getclogresult(d,channel)
    return l

#处理dsclog日志
class Register():

    def getdsclogpath(self,date):
        self.date = date
        dclogname = '-'.join(self.date) + '.log'
        dscflog = dsclogbase + '/' + dclogname
        return dscflog

    def getdsdata(self,channel):
        self.channel = channel
        self.contentlist = []
        for tag in regtaglist:
            reg = re.compile(r'%s\|(.*)\|(.*)\|(.*)\|0\|%s' % (channel,tag))
            f = open(self.getdsclogpath(date),'r')
            fr = f.read()
            f.close()
            r = re.findall(reg,fr)
            contentdetail = {'tag':tag,'total':len(r)}
            self.contentlist.append(contentdetail)
        return self.contentlist

    def dsclogrun(self):
        self.detaillist = []
        for channel in channellist:
            detail = {'channel':channel,'content':self.getdsdata(channel)}
            self.detaillist.append(detail)
        dsclogdata = {'detail':self.detaillist}
        return dsclogdata

#保存相关数据至数据库
def savedata():
    registerdata = Register()
    dfclogs.insert(dict(registerdata.dsclogrun(),**createtime))
    #dfclogs.update(createtime,{"$set":rundsdata(date)})

date = ('2014','08','24')
savedata()
# date = (sys.argv[1],sys.argv[2],sys.argv[3])