#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Login.py
# @Author: Feng
# @Date  : 2018/6/23
# @User  : tanjun
# @Desc  : 登陆一系列操作

from com.utils.Client12306Utils import Client12306Utils
from com.service.check.CheckImg import CheckImg

class Login:
    def __init__(self):
        self.CheckImg = CheckImg()
        self.Client12306Utils = Client12306Utils()
    # 登陆
    def go(self,config):
        try:
            self.CheckImg.go(config)
            print "4.登陆"
            landingResponse = self.Client12306Utils.landing(config["http"], config["username"], config["password"])
            return landingResponse;
        except Exception,e:
            print "登陆异常,回到第一步"
            print e
            self.go(config)