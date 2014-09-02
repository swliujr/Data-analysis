import lelcs

def tagdata(date,DFCLOGBASE,LOGINTAGLIST):
    data = lelcs.runlelcs(date,DFCLOGBASE,LOGINTAGLIST)
    return data

def usercount(date,dfclogbase):
    filelist = lelcs.listfile(date,DFCLOGBASE)
    logincount={'login':len(filelist)}
    return logincount

# def meregdict():
#     print dict(tagdata(date,DFCLOGBASE,LOGINTAGLIST),**usercount(date,dfclogbase))

# s_login = connection.data.s_login
# s_login.save(dict(lelcs.runlelcs(date,DFCLOGBASE,LOGINTAGLIST),**createtime))