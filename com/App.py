#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : App.py
# @Author: Feng
# @Date  : 2018/6/23
# @User  : tanjun
# @Desc  :
from com.service.login.Login import Login
from com.utils.HttpClientUtils import HttpClientUtils
from com.test.CollectData import CollectData
from com.utils.Client12306Utils import Client12306Utils
config = { # 固定格式
    "username":"18569000038",
    "password":"tanjun19940709",
    "http": None # 这个session对象需要全程用来访问请求,因为验证通过是与session绑定的,再每次提交验证失败后会重新创建session为了防止出现复杂验证码
}
# 开始登陆
#login = Login()
#login.go(config)

# 用于采集数据的
collect = CollectData()
collect.go(config)

# u12306 = Client12306Utils();
# tickeList = u12306.queryTicke(config["http"],"2018-09-15","SZQ","ZZQ").get("data").get("result")
# for ticke in tickeList:
#     print ticke