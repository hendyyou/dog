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
from com.service.show.ShowTickeList import ShowTickeList
config = { # 固定格式
    "username":"",
    "password":"",
    "http": None # 这个session对象需要全程用来访问请求,因为验证通过是与session绑定的,再每次提交验证失败后会重新创建session为了防止出现复杂验证码
}

# 用于采集数据的
#collect = CollectData()
#collect.go(config)

#开始登陆
login = Login()
login.go(config)

#查票
show = ShowTickeList()
u12306 = Client12306Utils();
#config["http"] = HttpClientUtils()
tickeList = u12306.queryTicke(config["http"], "2018-11-10", "SZQ", "ZZQ")

#打印查票结果
show.showList(tickeList)  # 打印

#提交选票
for ticke in tickeList:
    ticke = ticke.encode("utf8")
    cols = ticke.split("|")
    if cols[3][0:1] == "G" and cols[11] == "Y":  # 只查询高铁 并且有票的第一张
        print "--------------------------选中的票是----------------------------"
        print "日期:" + cols[13] + \
              ",车次:" + cols[3] + \
              ",开车时间:" + cols[8] + \
              ",到达时间:" + cols[9] + \
              ",耗时:" + cols[10] + \
              ",是否有票" + cols[11] + \
              ",二等座:" + cols[30] + \
              ",一等座:" + cols[31] + \
              ",商务座/特等座:" + cols[32] + \
              ",无座:" + cols[26] + \
              ",ticketId:" + cols[0]

        #检查是否已登陆
        loginFlag = u12306.checkUser(config["http"])
        if loginFlag :
            u12306.submitTicket(config["http"],cols[0],"2018-11-10","深圳","株洲")
            userData = u12306.getPassenger(config["http"])
            print userData
        break;

