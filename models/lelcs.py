import re
import glob
from models.config import *

def runlelcs(date,dfclogbase,taglist):
    run = Lelcs(date,dfclogbase,taglist)
    return run.runlelcs()

def listfile(date,dfclogbase):
    str = '/'
    logpath = str.join([dfclogbase,str.join(date),str])
    return glob.glob('%s*' % logpath)

class Lelcs:

    def __init__(self,date,dfclogbase,taglist):
        self.date = date
        self.dfclogbase = dfclogbase
        self.taglist = taglist

    def slog(self,log):
        imgre = re.compile(reg)
        logfile = open(log,'r')
        flog = logfile.read()
        frlog = re.findall(imgre,flog)
        logfile.close
        return frlog

    def runlelcs(self):
        clogpath = listfile(self.date,self.dfclogbase)
        logindata = []
        global reg
        for tag in self.taglist:
            reg = r'\|1\|%s' % tag
            userloglist = filter(self.slog,clogpath)
            useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
            logindata.append({"tag":tag,"tatol":len(userloglist),"userid":useridlist})
        rdata = {"detail":logindata}
        return rdata