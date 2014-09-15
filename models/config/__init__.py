# -*- coding: UTF-8 -*-

##locale env
#DSCLOGBASE = '/home/allon/workspace/Data-analysis/constant'
#DFCLOGBASE = '/home/allon/workspace/Data-analysis/file'
##mongo db connect
#MQHOST = 'localhost'
#MQPORT = 27017
##mysql db connect
#MSHOST = '10.0.0.26'
#MSPORT = 3306
#MSUSERNAME = 'meet_user'
#MSPASSWORD = 'meet_user'
#MSDBNAME = 'meet'

#online env
DSCLOGBASE = '/home/work/baihe/fire/photo/clog/constant'
DFCLOGBASE = '/home/work/baihe/fire/photo/clog/file'
##保存数据库
MQHOST = 'localhost'
MQPORT = 27017
##聊天数据库
MCHOST = '172.16.4.227'
MCPORT = 27001
##业务数据库
MSHOST = '172.16.4.246'
MSPORT = 3306
MSUSERNAME = 'user_meet_r'
MSPASSWORD = 'xxxxxxxxxxxxx'
MSDBNAME = 'meet'

SQLINIT = 'set session group_concat_max_len=9999999'

REGTAGLIST = [
    'boot',
    'qq_logging_the_third_party',
    'renren_logging_the_third_party',
    'baihe_logging_the_third_party',
    'micro-blog_logging_the_third_party',
    'douban_logging_the_third_party'
]

LOGINTAGLIST = [
    'logging_mobile',
    'forget the password',
    'douban_logging_the_third_party',
    'sinweibo_logging_the_third_party',
    'txweibo_logging_the_third_party',
    'qq_logging_the_third_party',
    'renren_logging_the_third_party',
    'baihe_logging_the_third_party',
    'logging_automatic',
    'logging_interface_access'
]

ENCOUNTERTAGLIST = [
    'head_button_click_number',
    'encounter_popup_photo',
    'encounter_popup_invite'
]
LIKETAGLIST = [
    'like_each_other_button_click',
    'i_like_button_click',
    'like_me_button_click',
    'number_of_accessing_users'
]

SETINGTAGLIST = [
    'third_party_invitation_we_chat_friends',
    'third_party_invitation_we_chat_memory',
    'third_party_invitation_micro-blog',
    'third_party_invitation_qq_space',
    'third_party_invitation_douban',
    'third_party_invitation_short_message',
    'third_party_invitation_renren',
    'third_party_invitation_tecent_micro-blog',
    'my_edit_button_click_number'
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

#数据库中定义的注册来源
registersource = {
    'register_mobile': 0,
    'register_sinaweibo': 3
}
