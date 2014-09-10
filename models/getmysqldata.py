# -*- coding: UTF-8 -*-

import MySQLdb as mdb
import config

def getmysqldata(sqlinit,sql):
    con = mdb.connect(config.MSHOST,config.MSUSERNAME,config.MSPASSWORD,config.MSDBNAME)
    try:
        cur = con.cursor()
        cur.execute(sqlinit)
        cur.execute(sql)
        r = cur.fetchone()
        return "%s" % r
    finally:
        if con:
            con.close()