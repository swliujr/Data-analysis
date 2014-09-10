import lelcs

def tagdata(date,dfclogbase,logintaglist):
    data = lelcs.runlelcs(date,dfclogbase,logintaglist)
    return data

def usercount(date,dfclogbase):
    filelist = lelcs.listfile(date,dfclogbase)
    logincount={'login':len(filelist)}
    return logincount

def meregdict(date,dfclogbase,logintaglist):
    return dict(tagdata(date,dfclogbase,logintaglist),**usercount(date,dfclogbase))