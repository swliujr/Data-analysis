# -*- coding: UTF-8 -*-

import datetime
import time

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
ctime = str(today - oneday)
# ctime = time.strftime('%Y-%m-%d')

taglist = [
    'boot',
    'mobile phone users_register interface',
    'mobile phone verification code'
]

channellist = [
    '0001##android_1_y',
    '0002##android_16_y'
]

dsclogformat = {
        'servertime': 0,
        'clienttime': 1,
        'userid': 2,
        'clientversion': 3,
        'channelid': 4,
        'mobilemode': 5,
        'osversion': 6,
        'deviceid': 7,
        'type': 8,
        'tag': 9
}

#数据库中定义的注册来源
registersource = {
    "register_mobile": 0,
    "register_sinaweibo": 3
}
