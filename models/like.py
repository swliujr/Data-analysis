import lelcs

def tagdata(date,dfclogbase,liketaglist):
    data = lelcs.runlelcs(date,dfclogbase,liketaglist)
    return data