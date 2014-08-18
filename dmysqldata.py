# -*- coding: UTF-8 -*-
import os
from os.path import getsize
import pymongo
import MySQLdb as mdb
import simplejson as json
from itertools import product
from shareres import *
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

createtime = {'created':ctime}

#mysql数据库
host = config.get('mysql','host')
#port = config.getint('mysql','port')
username = config.get('mysql','username')
password = config.get('mysql','password')
dbname = config.get('mysql','dbname')

con = mdb.connect(host,username,password,dbname)

#mongo数据库
host = config.get('mongodb','host')
port = config.getint('mongodb','port')
connection=pymongo.Connection(host,port)
dfclogs = connection.data.dfclogs

def conmysql(sql):
    cur = con.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    return  "%s" % r

def insertmdata():
    rsource = registersource.keys()
    for c,r in product(channellist,rsource):
        sql = "set session group_concat_max_len=9999999;" \
              "select concat('{\"detail.%s.%s\":{\"total\": ',count(id),' , \"userid\": [',group_concat(id),']}}') " \
              "from meet_user " \
              "where channel regexp '(.*)%s(.*)' and " \
              "source=%d and " \
              "SUBSTR(ctime, 1, 10)=date_add(current_date(),interval -1 day)" % (c,r,c,registersource[r])
        queryresult = conmysql(sql)
        if queryresult == 'None':
            queryresult = '{"detail.%s.%s":{"total":0,"userid":[]}}' % (c,r)
        dq = json.loads(queryresult)
        dfclogs.update(createtime,{"$set":dq})
    if con:
        con.close()

insertmdata()
