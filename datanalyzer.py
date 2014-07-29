# -*- coding: UTF-8 -*-
import os
from os.path import getsize
import glob
import re
import MySQLdb as mdb
import time
import datetime
import pymongo

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
ctime = time.strftime('%Y-%m-%d %H:%M:%S')

#taglist
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
#constant log format
'''
2014-07-25 17:17:02|2014-07-27 17:17:02|3234799|3.2.4|0026##android_google_y|LG-D802|4.2.2|12E1F6CA1CB85EBA11042B9C8981D5AA|0|boot
'''
logformat = {
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

#dsclog save path
clogbase = '/home/allon/python/data/constant'

#dfclog save path
flogbase = '/home/allon/python/data/file'

# #online mysql
# con = mdb.connect('10.0.0.26','meet_user','meet_user','meet')
#
# #datanalyzer mysql
# scon = mdb.connect('10.0.0.26','meet_data','data_passwd','data')

#mongodb
connection=pymongo.Connection('localhost',27017)
db = connection.data
collection = db.data
dsclogs = db.dsclogs

#get dsclog save path
def getcflog(cd):
    lfname = '-'.join(cd) + '.log'
    cflog = clogbase + '/' + lfname
    return cflog

#dsclog datanalyzer
class Dclog:
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

def getssclogresult(date,lnum):
    date = list(date)
    cflog = getcflog(date)
    rclog = Dclog(cflog,lnum)
    return rclog.dcresult()

#dfclog datanalyzer
def listfile(fd):
    str = '/'
    logpath = str.join([flogbase,str.join(fd),str])
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
    #get userid
    userloglist = filter(slog,getclog)
    useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
    #return tag, tag content userid,userid count
    return keywords,useridlist,len(useridlist)

# #get online mysql data
def getchannel():
    try:
        cur = con.cursor()
        cur.execute("select count(*) from meet_user")
        usernum = cur.fetchone()
        return '%d' % usernum
    finally:
        if con:
            con.close()

# #save data to mysql 

# def savedate():
#     try:
#         cur = scon.cursor()
#         stmt = "insert into regchannel(channelid,download) values(%s,%s)"
#         cur.executemany(stmt,rclog.dcresult())
#         scon.commit()
#     finally:
#         if scon:
#             scon.close()

# dfclog everyday tag count all user
def gettagcount(d):
    tagcount = []
    for tag in taglist:
        tagcount.append(getclogresult(d,tag))
    return tagcount

#dsclog column count
def getsstagcount(d,k):
    return k,getssclogresult(d, logformat[k])

dsclog = dict([str(p[0]),str(p[1::])] for p in gettagcount(('2014','07','17')))
dsclogs.insert(dsclog)

#print getsstagcount(('2014','07','17'),'channelid')
