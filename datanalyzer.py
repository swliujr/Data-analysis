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

#tag列表
taglist = [
    'boot',  #点击app在启动过程触发
    'mobile phone users_register interface',  #进入手机注册界面触发
    'mobile phone verification code',  #点击获取验证码弹出二次确认提示框的确认按钮触发
    'micro-blog import',  #点击新浪导入按钮触发, 点击完成按钮进入绑定手机号码时触发
    'micro-blog registry access',  #进入新浪注册完善资料页触发
    'user fill details_registration_mobile',  #进入手机注册完善资料页触发
    'input mobile number_registration_micro-blog',  #新浪注册中的手机绑定点击完成绑定按钮触发
    'verification code_registration_mirco-blog',  #新浪注册中的手机绑定点击获取验证码二次确认弹出框的确认按钮触发
    'QQ_logging_the third party',  #点击qq图标按钮时候触发
    'renren_logging_the third party',  #点击人人图标按钮触发
    'baihe_logging_the third party',  #在百合登陆页面点击登陆按钮触发
    'micro-blog bindings window_logging_the third party',  #弹出微博引导提示框触发
    'logging_login_botton', #点击登陆首页登陆按钮触发
    'logging_mobile',  #点击登陆页的登陆按钮触发
    'verification code logging_mobile phone',  #点击验证码登陆按钮触发
    'forget the password',  #点击忘记密码触发
    'logging_the third party',  #点击第三方按钮后判断是老用户即触发
    'logging_automatic',  #启动时候判断没有退出登陆的情况即触发
    'logging_interface access',  #登陆界面的访问
    'logging_micro-blog button click',  #点击微博登陆按钮触发
    'logging_micro-blog automatic',  #点击新浪登陆判断本地有sina的token是触发
    'encounter_popup avatar',
    'encounter_popup photo',
    'encounter_popup invite',
    'encounter_popup binding sina',
    'encounter_tactics code',
    'show time'
]
#constant日志格式
'''
时时上传日志格式，例如：
2014-07-25 17:17:02|2014-07-27 17:17:02|3234799|3.2.4|0026##jianjian_android_google_y|LG-D802|4.2.2|12E1F6CA1CB85EBA11042B9C8981D5AA|0|boot
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

#客户端时时上传日志的路径
clogbase = '/home/allon/python/data/constant'

#客户端上传日志文件保存路径
flogbase = '/home/allon/python/data/file'

# #线上数据库
# con = mdb.connect('10.0.0.26','meet_user','meet_user','meet')
#
# #数据分析数据库
# scon = mdb.connect('10.0.0.26','meet_data','data_passwd','data')

#mongo数据库
connection=pymongo.Connection('localhost',27017)
db = connection.data
collection = db.data
dsclogs = db.dsclogs

#获取时时日志路径
def getcflog(cd):
    lfname = '-'.join(cd) + '.log'
    cflog = clogbase + '/' + lfname
    return cflog

#时时上伟日志数据椕分析
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

#分析定时上传日志
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
    #提取用户的userid
    userloglist = filter(slog,getclog)
    useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
    #返回tag,包含此tag的id,用户数量
    return keywords,useridlist,len(useridlist)

#查询业务数据库中的数据
def getchannel():
    try:
        cur = con.cursor()
        cur.execute("select count(*) from meet_user")
        usernum = cur.fetchone()
        return '%d' % usernum
    finally:
        if con:
            con.close()

#保存最终得出的统计数据至数据

def savedate():
    try:
        cur = scon.cursor()
        stmt = "insert into regchannel(channelid,download) values(%s,%s)"
        cur.executemany(stmt,rclog.dcresult())
        scon.commit()
    finally:
        if scon:
            scon.close()

# #统计每天所有客户中包括tag的个数
def gettagcount(d):
    tagcount = []
    for tag in taglist:
        tagcount.append(getclogresult(d,tag))
    return tagcount

#统计每天所有客户时时上传日志中包括每列关键字个数
def getsstagcount(d,k):
    return k,getssclogresult(d, logformat[k])

dsclog = dict([str(p[0]),str(p[1::])] for p in gettagcount(('2014','07','17')))
dsclogs.insert(dsclog)
# print gettagcount(('2014','07','17'))
# print dict([str(p[0]),str(p[1::])] for p in list(getsstagcount(('2014','07','17'),'channelid')))
print getsstagcount(('2014','07','17'),'channelid')