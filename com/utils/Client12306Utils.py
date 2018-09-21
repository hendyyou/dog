#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Client12306Utils.py
# @Author: Feng
# @Date  : 2018/9/14
# @User  : tanjun
# @Desc  : 12306一系列操作放在这里
from io import BytesIO

from PIL import Image
import json

from com.config.Config import Config


class Client12306Utils:
    # 下载验证图片
    def downloadimg(self, http):
        response = http.get(Config.downloadimgurl)
        image = Image.open(BytesIO(response.content))
        image.save(Config.localCheckImg)

    # 提交图片验证
    def submitCheck(self, http, position):
        param = {
            'login_site': 'E',  # 固定的
            'rand': 'sjrand',  # 固定的
            'answer': position  # 验证码对应的坐标，两个为一组，跟选择顺序有关,有几个正确的，输入几个
        }
        response = http.post(Config.submitimgurl, param)
        return json.loads(response.content)

    # 登陆
    def landing(self, http, username, password):
        param = {"username": username, "password": password, "appid": "otn"}
        response = http.post(Config.landingurl, param)
        return json.loads(response.content)

    # 查票 param= 日期 起点 终点
    def queryTicke(self,http,date,start,end):
        path = Config.queryTicketurl + \
               "?leftTicketDTO.train_date=" + date + \
               "&leftTicketDTO.from_station=" + start + \
               "&leftTicketDTO.to_station=" + end + \
               "&purpose_codes=ADULT" #默认成人票
        response = http.get(path)
        return json.loads(response.content).get("data").get("result")
