# -*- coding: UTF-8 -*-

dsclogbase = '/home/allon/workspace/Data-analysis/constant'
dfclogbase = '/home/allon/workspace/Data-analysis/file'

dftaglist = [
    'boot',
    'mobile phone users_register interface',
    'mobile phone verification code'
]

REGTAGLIST = [
    'boot',
    'qq_logging_the_third_party',
    'renren_logging_the_third_party',
    'baihe_logging_the_third_party',
    'micro-blog_logging_the_third_party',
    'douban_logging_the_third_party'
]

logintaglist = [
    'logging_mobile',
    'forget the password',
    'douban_logging_the_third_party',
    'renren_logging_the_third_party',
    'renren_logging_the_third_party',
    'renren_logging_the_third_party',
    'renren_logging_the_third_party',
    'renren_logging_the_third_party',
    'logging_automatic',
    'logging_interface_access'
]

CHANNELLIST = [
    # '0001##jianjian_android_jianjianapp_y',
    # '0002##jianjian_android_jianjian3g_y',
    # '0003##jianjian_android_jianjianweb_y',
    # '0032##jianjian_android_jianjianweb2_y',
    # '0004##jianjian_android_jianjian91jianjian_y',
    # '0005##jianjian_android_xiaomi_y',
    # '0006##jianjian_android_91_y',
    # '0007##jianjian_android_360bh_y',
    # '0009##jianjian_android_jf_y',
    '0011##jianjian_android_azhi_y',
    '0012##jianjian_android_zsyyh_y'
    # '0013##jianjian_android_tx_y',
    # '0014##jianjian_android_baidu_y ',
    # '0015##jianjian_android_aliyun_y',
    # '0016##jianjian_android_dangle_y'
    # '0017##jianjian_android_oppo_y',
    # '0019##jianjian_android_nd_y',
    # '0020##jianjian_android_mmy_y',
    # '0021##jianjian_android_uy_y',
    # '0022##jianjian_android_szm_y',
    # '0023##jianjian_android_wyyyzx_y',
    # '0024##jianjian_android_jingdong_y',
    # '0025##jianjian_android_meizu_y',
    # '0026##jianjian_android_google_y',
    # '0027##jianjian_android_huawei_y',
    # '0028##jianjian_android_gongguan01_y',
    # '0029##jianjian_android_wbweixin_y',
    # '0030##jianjian_android_qqkfpt_y',
    # '0031##jianjian_android_wbtykj_y',
    # '0033##jianjian_android_huodong_y',
    # '0034##jianjian_android_huodong2_y',
    # '0035##jianjian_android_huodong3_y',
    # '0036##jianjian_android_huodong4_y',
    # '0037##jianjian_android_huodong5_y',
    # '0038##jianjian_android_huodong6_y',
    # '0039##jianjian_android_huodong7_y',
    # '0040##jianjian_android_huodong8_y',
    # '0041##jianjian_android_huodong9_y',
    # '0042##jianjian_android_weibo_y',
    # '0043##jianjian_android_wooboo1_y',
    # '0044##jianjian_android_wooboo2_y',
    # '0045##jianjian_android_wooboo3_y',
    # '0046##jianjian_android_wooboo4_y',
    # '0047##jianjian_android_wooboo5_y',
    # '0051##jianjian_android_jianjian360ax_y',
    # '0050##jianjian_android_jianjian360mn_y',
    # '0052##jianjian_android_jianjian360jh_y',
    # '0102##jianjian_android_jianjian360ax2_y',
    # '0103##jianjian_android_jianjian360ax3_y',
    # '0104##jianjian_android_jianjian360ax4_y',
    # '0105##jianjian_android_jianjian360ax5_y',
    # '0106##jianjian_android_jianjian360ax6_y',
    # '0107##jianjian_android_jianjian360ax7_y',
    # '0108##jianjian_android_jianjian360ax8_y',
    # '0109##jianjian_android_jianjian360ax9_y',
    # '0110##jianjian_android_jianjian360ax10_y',
    # '0111##jianjian_android_jianjian360ax11_y',
    # '0115##jianjian_android_jianjianxiaomiax15_y',
    # '0116##jianjian_android_jianjianxiaomiax16_y'
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
    'register_mobile': 0,
    'register_sinaweibo': 3
}