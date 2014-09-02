import re
from models.config import *

def dsclogrun(date,dsclogbase,channellist,regtaglist):
    run = Register(date,dsclogbase,channellist,regtaglist)
    return run.dsclogrun()

class Register:
    def __init__(self,date,dsclogbase,channellist,regtaglist):
        self.date = date
        self.dsclogbase = dsclogbase
        self.channellist = channellist
        self.regtaglist = regtaglist

    def getdsclogpath(self,date,dsclogbase):
        dclogname = '-'.join(self.date) + '.log'
        dscflog = self.dsclogbase + '/' + dclogname
        return dscflog

    def getdsdata(self,channel):
        self.channel = channel
        self.contentlist = []
        for tag in self.regtaglist:
            reg = re.compile(r'%s\|(.*)\|(.*)\|(.*)\|0\|%s' % (channel,tag))
            f = open(self.getdsclogpath(self.date,self.dsclogbase),'r')
            fr = f.read()
            f.close()
            r = re.findall(reg,fr)
            contentdetail = {'tag':tag,'total':len(r)}
            self.contentlist.append(contentdetail)
        return self.contentlist

    def dsclogrun(self):
        self.detaillist = []
        for channel in self.channellist:
            detail = {'channel':channel,'content':self.getdsdata(channel)}
            self.detaillist.append(detail)
        dsclogdata = {'detail':self.detaillist}
        return dsclogdata