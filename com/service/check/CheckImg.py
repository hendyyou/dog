#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : self.py
# @Author: Feng
# @Date  : 2018/9/14
# @User  : tanjun
# @Desc  : 下载验证码并验证一系列操作

from com.utils.Client12306Utils import Client12306Utils
from com.baidu.Matching import Matching
from com.utils.HttpClientUtils import HttpClientUtils

from com.utils.CuttingUtils import CuttingUtils
class CheckImg:
    def __init__(self):
        self.Client12306Utils = Client12306Utils()
        self.Matching = Matching()
        self.CuttingUtils = CuttingUtils()
    # 下载图片验证码并裁剪
    def downloadimg(self,config):
        print "1.下载图片验证码"
        try:
            self.Client12306Utils.downloadimg(config["http"])
            print "下载图片验证码成功,继续下一步"
            self.CuttingUtils.go() # 裁剪图片
            return self.getPosition(config)
        except Exception, e:
            print "下载图片验证码异常,重新尝试"
            print e
            config["http"] = HttpClientUtils() # 重新设置http对象 防止出现复杂验证码
            return self.downloadimg(config)

    # 获取图片验证位置
    def getPosition(self,config):
        print "2.获取图片验证码答案"
        try:
            # 1从百度获取答案
            answer = self.Matching.go()
            if answer == None:
                print "无法识别图片验证码答案,回到第一步"
                return self.downloadimg(config)
            print "获取图片验证码答案成功,继续下一步"
            return self.submitCheck(config,answer)
        except Exception, e:
            print "获取图片验证码答案异常,重新尝试"
            print e
            return self.getPosition(config)


    # 提交图片验证
    def submitCheck(self,config,answer):
        print "3.提交图片验证码答案"
        try:
            checkResponse = self.Client12306Utils.submitCheck(config["http"],answer.get("offset"))
            if checkResponse.get("result_code") == "4":  # 验证码 验证成功,开始执行登陆
                print "验证成功"
                return answer
            else:
                print "验证失败,回到第一步"
                return self.downloadimg(config)
        except Exception, e:
            print "提交图片验证码答案异常,回到第一步"
            print e
            return self.downloadimg(config)

    # 开始下载验证码并提交验证
    def go(self,config):
        return self.downloadimg(config)
