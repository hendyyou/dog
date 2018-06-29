#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Session.py
# @Author: Feng
# @Date  : 2018/6/25
# @User  : tanjun
# @Desc  : 创建一个整体使用的session对象
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# http 请求工具
class Http:
    def __init__(self):
        self.httpJson = {
            "session": requests.session(),
            "headers": {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://kyfw.12306.cn",
                "Referer": "https://kyfw.12306.cn/otn/login/init",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
        }
    # 发出http get 请求
    def get(self,url):
        session = self.httpJson.get("session")
        return session.get(url=url)

    # 发送http post 请求
    def  post(self,url,data):
        session = self.httpJson.get("session")
        return session.post(url=url,data=data,headers=self.httpJson.get("headers"),verify=False)

