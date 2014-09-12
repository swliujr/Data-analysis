import config
import pymongo
import datetime
import subprocess

del1 = datetime.timedelta(days=1)
del2 = datetime.timedelta(days=2)

oy = int((datetime.date.today() - del2).strftime("%Y"))
om = int((datetime.date.today() - del2).strftime("%m"))
od = int((datetime.date.today() - del2).strftime("%d"))
yy = int((datetime.date.today() - del1).strftime("%Y"))
ym = int((datetime.date.today() - del1).strftime("%m"))
yd = int((datetime.date.today() - del1).strftime("%d"))

start = datetime.datetime(oy,om,od,16,0,0)
end = datetime.datetime(yy,ym,yd,16,0,0)

connection = pymongo.Connection(config.MCHOST,config.MCPORT)
db = connection.immessage

chat_visits_number = db.immessage.find({"date":{"$gte":start,"$lt":end}}).count()
number_of_chat_visitor = db.immessage.find({"date":{"$gte":start,"$lt":end}})

l = []
for n in db.immessage.find({"date":{"$gte":start,"$lt":end}},{"sender":1,"_id":0}):
    l.append(tuple(n.values()))

def rundata():
    detail = []
    detail.append({"tag":"chat_visits","total":chat_visits_number})
    detail.append({"tag":"number_of_chat_visitor","total":len(set(l))})
    detail.append({"tag":"number_of_per_capita_chat","total":chat_visits_number/len(set(l))})
    result = {"detail":detail}
    return result