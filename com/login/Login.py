#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Login.py
# @Author: Feng
# @Date  : 2018/6/23
# @User  : tanjun
# @Desc  : 登陆处理类
from PIL import Image
from io import BytesIO
import json
from com.image.ImageInterfere import Cutting
from com.session.Session import Http

# 整套登陆流程
class Login:
    def __init__(self):

        self.downloadimgurl = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand";  # 验证码图片下载地址
        self.submitimgurl = "https://kyfw.12306.cn/passport/captcha/captcha-check";  # 图片验证码提交地址
        self.landingurl = "https://kyfw.12306.cn/passport/web/login"  # 登陆地址
        self.checkimgname = "img/checkimg.jpg"  # 验证码图片名称
        self.cutting = Cutting() # 图片验证服务
        self.http = Http()

    # 下载图片验证码
    def downloadimg(self):
        print "1.下载图片验证码"
        try:
            response = self.http.get(self.downloadimgurl)
            image = Image.open(BytesIO(response.content))
            image.save(self.checkimgname)
        except Exception:
            print "下载图片验证码异常,重新尝试"
            print e
            self.downloadimg()
        else:
            print "下载图片验证码成功,继续下一步"
            self.getPosition()

    # 获取图片验证位置
    def getPosition(self):
        print "2.获取图片验证码答案"
        try:
            offset = self.cutting.go(self.checkimgname)
            if offset == None:
                print "无法识别图片验证码答案,回到第一步"
                self.downloadimg()
            self.position = offset
        except Exception,e:
            print "获取图片验证码答案异常,重新尝试"
            print e
            self.getPosition()
        else:
            print "获取图片验证码答案成功,继续下一步"
            self.submitCheck()


    # 提交图片验证
    def submitCheck(self):
        print "3.提交图片验证码答案"
        try:
            param = {
                'login_site': 'E',  # 固定的
                'rand': 'sjrand',  # 固定的
                'answer': self.position  # 验证码对应的坐标，两个为一组，跟选择顺序有关,有几个正确的，输入几个
            }
            response = self.http.post(self.submitimgurl, param)
            msg = json.loads(response.content)
            self.checkResponse = msg
        except Exception:
            print "提交图片验证码答案异常,回到第一步"
            print e
            self.downloadimg()
        else:
            if self.checkResponse.get("result_code") == "4":  # 验证码 验证成功,开始执行登陆
                print "验证成功,继续下一步"
                self.landing()
            else:
                print "验证失败,回到第一步"
                self.http = Http() # 换一下session 防止出现较难的验证码
                self.downloadimg()

    # 登陆
    def landing(self):
        print "4.登陆"
        try:
            param = {"username": self.username, "password": self.password, "appid": "otn"}
            response = self.http.post(self.landingurl,param)
            self.landingResponse = json.loads(response.content)
        except Exception,e:
            print "登陆异常,回到第一步"
            print e
            self.downloadimg()
        else:
            print self.landingResponse.get("result_message")

    # 执行一系列操作
    def go(self,username,password):
       self.username = username
       self.password = password
       self.downloadimg()