# -*- coding: UTF-8 -*-

import lelcs
import getmysqldata
import simplejson as json
import re

import config
tag = 'show_time'

left_draw_record = "select concat('{\"tag\":\"left_draw_record\",\"tatol\":',count(user_id),',\"userid\":[',group_concat(distinct(user_id)),']}')" \
                        "from meet_dislike " \
                        "where substr(from_unixtime(dateline),1,10) = '2014-07-10'"
right_draw_record = "select concat('{\"tag\":\"right_draw_record\",\"tatol\":',count(user_id),',\"userid\":[',group_concat(distinct(user_id)),']}') " \
                        "from meet_like " \
                        "where substr(from_unixtime(dateline),1,10) = '2014-07-10'"
matching_successs_number = "select concat('{\"tag\":\"matching_successs_number\",\"total\":',count(lid),',\"userid\":[',group_concat(distinct(user_id)),']}') " \
                           "from meet_like " \
                           "where substr(from_unixtime(like_dateline),1,10)='2014-02-25'"
contact_list = "select concat('{\"tag\":\"contact_list\",\"total\":',count(cid),',\"userid\":[',group_concat(distinct(user_id)),']}')" \
                " from meet_contacts " \
                "where substr(from_unixtime(ctime),1,10) = '2014-07-03'"
head_examine = "select concat('{\"tag\":\"head_examine\",\"total\":',count(id),',\"userid\":[',group_concat(id),']}') " \
               "from meet_user " \
               "where substr(ctime,1,10)='2014-09-01' and substr(mobile,1,1)!='w' and avatar_status=3"
photo_number = "select concat('{\"tag\":\"photo_number\",\"total\":',count(id),',\"userid\":[',group_concat(user_id),']}') " \
               "from meet_user_photo " \
               "where substr(ctime,1,10)='2014-09-01'"
personal_data_not_complete = "select concat('{\"tag\":\"personal_data_not_complete\",\"total\":',count(id),',\"userid\":[',group_concat(id),']}') " \
                             "from meet_user " \
                             "where step!=0 and substr(mobile,1,1)!='w' and substr(ctime,1,10)='2014-09-01'"
#get show time data
def filelist(date,dfclogbase):
    filelist = lelcs.listfile(date,dfclogbase)
    return filelist

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

def getclogresult(date,dfclogbase):
    date = list(date)
    getclog = filelist(date,dfclogbase)
    userloglist = map(slog,getclog)
    return userloglist

#get tag data

def tagdata(date,dfclogbase,encountertaglist):
    data = lelcs.runlelcs(date,dfclogbase,encountertaglist)
    return data

def getdata(sql):
    result = getmysqldata.getmysqldata(config.SQLINIT,sql)
    return result

def jtod(s):
    return json.loads(getdata(s))

def meregdict(date,dfclogbase,encountertaglist):
    sqllist = []
    rl = []
    t = tagdata(date,dfclogbase,encountertaglist)
    for d in jtod(left_draw_record),jtod(right_draw_record),jtod(matching_successs_number),jtod(contact_list),jtod(photo_number),jtod(head_examine),jtod(personal_data_not_complete):
        sqllist.append(d)
    rl = t.values()[0]
    result={"detail":rl+sqllist}
    return result
