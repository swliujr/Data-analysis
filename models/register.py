import re
from config import *

class Register:
    def __init__(self,date):
        self.date = date

    def getdsclogpath(self,date):
        dclogname = '-'.join(self.date) + '.log'
        dscflog = dsclogbase + '/' + dclogname
        return dscflog

    def getdsdata(self,channel):
        self.channel = channel
        self.contentlist = []
        for tag in REGTAGLIST:
            reg = re.compile(r'%s\|(.*)\|(.*)\|(.*)\|0\|%s' % (channel,tag))
            f = open(self.getdsclogpath(self.date),'r')
            fr = f.read()
            f.close()
            r = re.findall(reg,fr)
            contentdetail = {'tag':tag,'total':len(r)}
            self.contentlist.append(contentdetail)
        return self.contentlist

    def dsclogrun(self):
        self.detaillist = []
        for channel in CHANNELLIST:
            detail = {'channel':channel,'content':self.getdsdata(channel)}
            self.detaillist.append(detail)
        dsclogdata = {'detail':self.detaillist}
        return dsclogdata