#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : IdentifyImg.py
# @Author: Feng
# @Date  : 2018/11/6
# @User  : tanjun
# @Desc  : 从数据库中识别本次的图片验证

from com.config.Config import Config
from com.utils.MysqlUtils import MysqlUtils
import hashlib

class IdentifyImg:
    def __init__(self):
        self.answersSql = "select chinese from answers where md5 = %s"
        self.questionsSql = "select chinese from questions where md5 = %s"
        self.MysqlUtils = MysqlUtils()

    def getAnswers(self,name):
        cursor = self.MysqlUtils.querySql(self.answersSql,(name))
        if cursor.rowcount != 0:
            return cursor.fetchall()[0].get("chinese")
        return None

    def getQuestions(self,name):
        cursor = self.MysqlUtils.querySql(self.questionsSql, (name))
        if cursor.rowcount != 0:
            return cursor.fetchall()[0].get("chinese")
        return None

    # 获取一个路径中的文件的md5
    def md5(self, url):
        fd = open(url, "r")
        fcont = fd.read()
        fmd5 = hashlib.md5(fcont)
        return fmd5.hexdigest()

    # 精准匹配
    def accurate(self, questionsName, answersName):
        if questionsName == j:
            return j
        return False

    # 分词匹配 一个中文占3个长度
    def participle(self, questionsName, answersName):
        qusize = len(questionsName)
        ansize = len(answersName)
        for i in range(0, qusize, 3):
            p = questionsName[i:i + 3]
            for k in range(0, ansize, 3):
                a = j[k:k + 3]
                if (p == a):
                    return j
        return

    # 综合所有情况匹配验证码答案
    def all(self, questionsName, answers):
        answerStr = ""
        chineseStr = ""
        for i in range(8):
            temp = self.accurate(questionsName, answers[i])  # 精确匹配
            if temp == False:
                temp = self.participle(questionsName, answers[i])  # 分词匹配
                if temp != False:  # 最终匹配成功
                    answerStr = answerStr + Config.imgOrderPosition.get(str(i + 1)) + ","
                    chineseStr = chineseStr + temp + ","
            if answerStr == "":
                return None
            else:
                return {"offset": answerStr[0:-1], "chinese": chineseStr[0:-1]}

    def go(self):
        try:
            # 1识别提问
            questionsName = self.getQuestions((self.md5(Config.localproblemimgUrl)))
            if questionsName == None : #无法识别
                return None
            # 2识别回答
            answers = []
            for i in range(8):
                answersName = self.getAnswers((self.md5(Config.localimgpath + str(i + 1) + Config.imgSuffix)))
                if answersName != None:
                    answers.append(answersName)
            # 3匹配答案
            ret = self.all(retOcr, answers)
            if ret != None:
                ret["retOcr"] = retOcr
                ret["answers"] = answers
            return ret
        except:
            return self.go()