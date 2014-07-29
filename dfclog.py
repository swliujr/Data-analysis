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

#tag列表
taglist = [
    'boot',
    'mobile phone users_register interface',
    'mobile phone verification code',
    'micro-blog import',
    'micro-blog registry access',
    'user fill details_registration_mobile',
    'input mobile number_registration_micro-blog',
    'verification code_registration_mirco-blog',
    'QQ_logging_the third party',
    'renren_logging_the third party',
    'baihe_logging_the third party',
    'micro-blog bindings window_logging_the third party',
    'logging_login_botton',
    'logging_mobile',
    'verification code logging_mobile phone',
    'forget the password',
    'logging_the third party',
    'logging_automatic',
    'logging_interface access',
    'logging_micro-blog button click',
    'logging_micro-blog automatic',
    'encounter_popup avatar',
    'encounter_popup photo',
    'encounter_popup invite',
    'encounter_popup binding sina',
    'encounter_tactics code',
    'show time'
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

#获取时时日志路径
def getdfclog(cd):
    lfname = '-'.join(cd) + '.log'
    cflog = clogbase + '/' + lfname
    return cflog

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

def getclogresult(date,keywords):
    global reg
    reg = r'\|1\|%s' % keywords
    date = list(date)
    getclog = listfile(date)
    #提取用户的userid
    userloglist = filter(slog,getclog)
    useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
    #返回tag,包含此tag的id,用户数量
    return keywords,{'userid': useridlist , 'total': len(useridlist)}

# 统计每天所有客户中包括tag的个数
def gettagcount(d):
    tagcount = []
    for tag in taglist:
        tagcount.append(getclogresult(d,tag))
    return tagcount
    
# 将结果保存至数据库
def savedata(d):
    dfclogdata = dict([str(p[0]),str(p[1])] for p in gettagcount(('2014','07','17')))
    r = {'details':dfclogdata,'created':ctime}
    dfclogs.insert(r)

savedata(('2014','07','17'))
