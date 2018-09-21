#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Config.py
# @Author: Feng
# @Date  : 2018/9/14
# @User  : tanjun
# @Desc  : 各参数配置
import pymysql


class Config:
    imgSuffix = ".png"
    downloadimgurl = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"  # 验证码图片下载地址 get
    submitimgurl = "https://kyfw.12306.cn/passport/captcha/captcha-check"  # 图片验证码提交地址 post
    landingurl = "https://kyfw.12306.cn/passport/web/login"  # 登陆地址 post
    queryTicketurl = "https://kyfw.12306.cn/otn/leftTicket/queryA" # 查票地址 get 需要带明文条件
    localimgpath = "/Users/tanjun/Desktop/img/"  # 本地图片缓存的绝对路径
    localproblemimgUrl = localimgpath + "problem" + imgSuffix  # 本地缓存验证码提问图片名称
    localCheckImg = localimgpath + "checkimg" + imgSuffix  # 验证码图片保存名称
    mysqlconfig = { # mysql 数据库连接配置
        "host": "118.126.102.79",
        "port": 3306,
        "user": "root",
        "password": "tanjun1994",
        "db": "tanjun",
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
    }
    # 图片顺序对应位置坐标
    imgOrderPosition = {
        "1": "35,35",
        "2": "105,35",
        "3": "175,35",
        "4": "245,35",
        "5": "35,105",
        "6": "105,105",
        "7": "175,105",
        "8": "245,105"
    }
    # 位置对应图片顺序
    positionImgOrder = {
        "35,35": "1",
        "105,35": "2",
        "175,35": "3",
        "245,35": "4",
        "35,105": "5",
        "105,105": "6",
        "175,105": "7",
        "245,105": "8"
    }