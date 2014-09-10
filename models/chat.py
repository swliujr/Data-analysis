
db.immessage.find({"date":{"$gt":ISODate("2014-09-08T16:00:00.000Z"),"$lt":ISODate("2014-09-09T16:00:00.000Z")}}).count()
db.immessage.distinct("sender",{"date":{"$gt":ISODate("2014-09-08T16:00:00.000Z"),"$lt":ISODate("2014-09-09T16:00:00.000Z")}}).length