class Login:

    def listfile(self,fd):
        str = '/'
        logpath = str.join([dfclogbase,str.join(fd),str])
        return glob.glob('%s*' % logpath)

    def slog(log):
        imgre = re.compile(reg)
        logfile = open(log,'r')
        flog = logfile.read()
        frlog = re.findall(imgre,flog)
        logfile.close
        return frlog

    def getclogresult(date,channel):
        date = list(date)
        getclog = listfile(date)
        r = {}
        global reg
        for tag in dftaglist:
            reg = r'%s(.*)1\|%s' % (channel,tag)
            userloglist = filter(slog,getclog)
            useridlist = map((lambda x: x.split('_')[1].split('.')[0]),userloglist)
            r[tag] = {"userid":useridlist,"total":len(useridlist)}
        return r