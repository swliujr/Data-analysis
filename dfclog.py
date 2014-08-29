# -*- coding: UTF-8 -*-
import os,sys
from os.path import getsize
import glob
import re
import pymongo
import simplejson as json
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
    for tag in taglist:
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

#处理dsclog日志，获取app启动次数
def getdsclogpath(date):
    lfname = '-'.join(date) + '.log'
    cflog = dsclogbase + '/' + lfname
    return cflog

def getdsdata(channel,date,tag):
    reg = r'%s\|(.*)\|(.*)\|(.*)\|0\|%s' % (channel,tag)
    reg = re.compile(reg)
    f = open(getdsclogpath(date),'r')
    flog = f.read()
    frlog = re.findall(reg,flog)
    f.close()
    return len(frlog)

def rundsdata(date):
    l = {}
    for channel,tag in product(channellist,dstaglist):
        k = '%s.%s.%s.%s' % ('detail',channel,tag,'total')
        l[k] = getdsdata(channel,date,tag)
    return l

#保存相关数据至数据库
def savedata(date):
    dfclogdata = {}
    dfclogdata['detail'] = rundfdata(date)
    dfclogs.insert(dict(dfclogdata,**createtime))
    dfclogs.update(createtime,{"$set":rundsdata(date)})

date = (sys.argv[1],sys.argv[2],sys.argv[3])
savedata(date)
