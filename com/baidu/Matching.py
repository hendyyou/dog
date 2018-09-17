#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Matching.py
# @Author: Feng
# @Date  : 2018/6/28
# @User  : tanjun
# @Desc  : 百度匹配答案
from com.baidu.ClassifyApi import ClassifyApi
from com.baidu.OcrApi import OcrApi
from com.config.Config import Config


class Matching:
    def __init__(self):
        self.ClassifyApi = ClassifyApi();
        self.OcrApi = OcrApi();

    # 精准匹配 只匹配 keyword 中的值
    def accurate(self,problemStr,answer):
        if len(answer) == 0:
            return False
        for j in answer:
            if problemStr == j.get("keyword"):
                return j.get("keyword")
        return False

    # 分词匹配 只匹配 keyword 中的值 一个中文占3个长度
    def participle(self,problemStr,answer):
        strsize = len(problemStr)
        if strsize == 0:
            return False
        for i in range(0, strsize, 3):
            for j in answer:
                ansize = len(j.get("keyword"))
                if ansize == strsize:  # 长度是否一致
                    p = problemStr[i:i + 3]
                    for k in range(0,ansize,3):
                        a = j.get("keyword")[k:k + 3]
                        if(p == a):
                            return j.get("keyword")
        return False

    # 综合所有情况匹配验证码答案
    def all(self,problemStr,answers):
        answerStr = ""
        chineseStr = ""
        for i in range(8):
            temp = self.accurate(problemStr,answers[i]) # 精确匹配
            if temp == False:
                temp = self.participle(problemStr, answers[i]) # 分词匹配

            if temp != False: # 最终匹配成功
                answerStr = answerStr + Config.imgOrderPosition.get(str(i + 1)) + ","
                chineseStr = chineseStr + temp + ","
        if answerStr == "":
            return None
        else:
            return {"offset":answerStr[0:-1],"chinese":chineseStr[0:-1]}

    # 执行百度识别图片并返回答案
    def go(self):
        try:
            # 1识别提问
            retOcr = self.OcrApi.ocr(Config.localproblemimgUrl)
            if retOcr == None : #无法识别
                return None
            # 2识别回答
            answers = []
            for i in range(8):
                retClassify = self.ClassifyApi.classify(Config.localimgpath + str(i + 1) + Config.imgSuffix)
                answers.append(retClassify)
            # 3匹配答案
            ret = self.all(retOcr, answers)
            if ret != None:
                ret["retOcr"] = retOcr
                ret["answers"] = answers
            return ret
        except:
            return self.go()