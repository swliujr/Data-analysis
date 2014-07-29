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

# 线上数据库
con = mdb.connect('10.0.0.26','user','password','lite')

# 数据分析数据库
scon = mdb.connect('10.0.0.26','user','password','data')


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

#保存最终得出的统计数据至mysql数据库

def savedate():
    try:
        cur = scon.cursor()
        stmt = "insert into regchannel(channelid,download) values(%s,%s)"
        cur.executemany(stmt,rclog.dcresult())
        scon.commit()
    finally:
        if scon:
            scon.close()
