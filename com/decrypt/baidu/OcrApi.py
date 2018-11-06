#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : OcrApi.py
# @Author: Feng
# @Date  : 2018/6/27
# @User  : tanjun
# @Desc  : 调用百度图片识别文字
from aip import AipOcr

class OcrApi:
    def __init__(self):
        APP_ID = "11453980"
        API_KEY = "Pgn8sAUBngAq0TyoeVAxuFME"
        SECRET_KEY = "ZkgXwxko90DRBsYtvTE3bnLmI9fr6PLo"
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 调用传入验证码提问裁剪图片地址,访问api返回识别中文
    def ocr(self,url):
        try:
            image = open(url, 'rb').read()
            msg = self.client.basicAccurate(image)
            words_result = msg.get("words_result")
            if words_result != None:  # 会存在 api调用次数上线,不返回数据了
                u = words_result[0].get("words")
                return u.encode("utf-8")
            else:
                return None
        except Exception,e:
            print e
            raise RuntimeError("百度api调用异常")