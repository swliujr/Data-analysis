# -*- coding: UTF-8 -*-
import os,sys
from os.path import getsize
import glob
import re
import pymongo
from shareres import *
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

createtime = {'created':ctime}

#客户端上传日志路径
dfclogbase = config.get('general','dfclogbase')

#连接mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
dfclogs = connection.data.dfclogs

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

#查询业务数据库中的数据
def conmysql(sql):
    cur = con.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    return  "%s" % r

def savedata(d):
    r = {}
    r['detail'] = getchannelr(d)
    dfclogs.insert(dict(r,**createtime))

date = (sys.argv[1],sys.argv[2],sys.argv[3])
savedata(date)
