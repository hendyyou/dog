#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ClassifyApi.py
# @Author: Feng
# @Date  : 2018/6/27
# @User  : tanjun
# @Desc  : 调用百度图片识别
from aip import AipImageClassify

class BApiClassify:
    def __init__(self):
        APP_ID = "11455535"
        API_KEY = "oGUA2c9R2CjWFnrKTCSHLbTY"
        SECRET_KEY = "qy6QqdUsfNs5cmRys9RX2cECo0H2vjX3"
        self.client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    # 识别图片有可能叫什么
    def classify(self,url):
        image = open(url, 'rb').read()
        msg = self.client.advancedGeneral(image)
        rets = []
        result = msg.get("result")
        if result != None: # 会存在 api调用次数上线,不反悔数据了
            for i in result:
                temp = {"root": i.get("root").encode("utf-8"), "keyword": i.get("keyword").encode("utf-8"),
                        "score": float(i.get("score"))}
                rets.append(temp)
        return rets