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

#统计每个用户在一天中所有showtime的平均值

#需要统计的tag
tag = 'show time'

#定义时间字段，存储mongo记录时使用
createtime = {'created':ctime}

#客户端上传日志文件保存路径
dfclogbase = config.get('general','dfclogbase')

#mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
showtime = connection.data.showtime

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
    showtime.insert(dict(r,**createtime))

date = (sys.argv[1],sys.argv[2],sys.argv[3])
savedata(date)
