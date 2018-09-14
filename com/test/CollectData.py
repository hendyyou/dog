#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CollectData.py
# @Author: Feng
# @Date  : 2018/9/14
# @User  : tanjun
# @Desc  : 收集验证数据

from com.utils.Client12306Utils import Client12306Utils
from com.service.check.CheckImg import CheckImg
from com.config.Config import Config
from com.utils.MysqlUtils import MysqlUtils
class CollectData:
    def __init__(self):
        self.CheckImg = CheckImg()
        self.Client12306Utils = Client12306Utils()
        self.MysqlUtils = MysqlUtils()
    # 登陆
    def go(self,config):
        try:
            answer = self.CheckImg.go(config)
            #sqls = self.getMd5(answer)
            #self.writeDb(sqls)
        except Exception,e:
            print "保存到数据库异常,回到第一步"
            print e
            self.go(config)

    # 获取图片md5值,并生成sql
    def getMd5(self,answer):
        print "4.获取图片md5值"
        sqls = []
        # 1.将提问图片获取md5值 并插入数据库
        print "提问-------------------------------提问"
        qmd5 = self.md5(Config.localproblemimgUrl)
        print "中文：" + answer["retOcr"] + "，md5：" + qmd5
        sqls.append({"sql": "insert into questions(md5,chinese) values(%s,%s)", "param": (qmd5, answer["retOcr"])})
        # 2.将回答图片获取md5值 并插入数据库
        print "回答-------------------------------回答"
        offset = answer["offset"].split(",")
        chinese = answer["chinese"].split(",")
        for i in range(0, len(offset), 2):
            str = offset[i] + "," + offset[i + 1]
            amd5 = self.md5(Config.localimgpath + Config.positionImgOrder.get(str) + ".png")
            print "中文：" + chinese[i / 2] + "，md5：" + amd5
            sqls.append({"sql": "insert into answers(md5,chinese) values(%s,%s)", "param": (amd5, chinese[i / 2])})
        return sqls

    # 写入数据库
    def writeDb(self,sqls):
        print "5.写入数据库"
        self.MysqlUtils.addSql(sqls)

    # 获取一个路径中的文件的md5
    def md5(self,url):
        fd = open(url, "r")
        fcont = fd.read()
        fmd5 = hashlib.md5(fcont)
        return fmd5.hexdigest()