class Register:

    def getdsclogpath(self,date):
        self.date = date
        dclogname = '-'.join(self.date) + '.log'
        dscflog = dsclogbase + '/' + dclogname
        return dscflog

    def getdsdata(self,channel):
        self.channel = channel
        self.contentlist = []
        for tag in regtaglist:
            reg = re.compile(r'%s\|(.*)\|(.*)\|(.*)\|0\|%s' % (channel,tag))
            f = open(self.getdsclogpath(date),'r')
            fr = f.read()
            f.close()
            r = re.findall(reg,fr)
            contentdetail = {'tag':tag,'total':len(r)}
            self.contentlist.append(contentdetail)
        return self.contentlist

    def dsclogrun(self):
        self.detaillist = []
        for channel in channellist:
            detail = {'channel':channel,'content':self.getdsdata(channel)}
            self.detaillist.append(detail)
        dsclogdata = {'detail':self.detaillist}
        return dsclogdata