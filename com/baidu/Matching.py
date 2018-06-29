#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Matching.py
# @Author: Feng
# @Date  : 2018/6/28
# @User  : tanjun
# @Desc  : 匹配问题和答案

class Matching:
    def __init__(self):
        # 位置对应坐标点
        self.position = {
            "1": "35,35",
            "2": "105,35",
            "3": "175,35",
            "4": "245,35",
            "5": "35,105",
            "6": "105,105",
            "7": "175,105",
            "8": "245,105"
        }

    # 精准匹配 只匹配 keyword 中的值
    def accurate(self,problemStr,answer):
        for j in answer:
            if problemStr == j.get("keyword"):
                return True
        return False

    # 分词匹配 只匹配 keyword 中的值 一个中文占3个长度
    def participle(self,problemStr,answer):
        strsize = len(problemStr)
        for i in range(0, strsize, 3):
            for j in answer:
                ansize = len(j.get("keyword"))
                if ansize == strsize:  # 长度是否一致
                    p = problemStr[i:i + 3]
                    for k in range(0,ansize,3):
                        a = j.get("keyword")[k:k + 3]
                        if(p == a):
                            return True
        return False

    # 综合所有情况匹配验证码答案
    def go(self,problemStr,answers):
        answerStr = ""
        for i in range(8):
            temp = False
            if self.accurate(problemStr,answers[i]): # 精确匹配成功
                temp = True
            elif self.participle(problemStr, answers[i]): # 分词匹配成功
                temp = True
            if temp: # 最终匹配成功
                answerStr = answerStr + self.position.get(str(i + 1)) + ","
        if answerStr == "":
            return None
        else:
            return answerStr[0:-1]