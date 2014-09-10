import lelcs

def tagdata(date,dfclogbase,setingtaglist):
    data = lelcs.runlelcs(date,dfclogbase,setingtaglist)
    return data