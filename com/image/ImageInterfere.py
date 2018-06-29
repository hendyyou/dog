#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ImageInterfere.py
# @Author: Feng
# @Date  : 2018/6/27
# @User  : tanjun
# @Desc  : 对验证码图片进行处理
from PIL import Image
from com.baidu.OcrApi import BApiOcr
from com.baidu.ClassifyApi import BApiClassify
from com.baidu.Matching import Matching

class Cutting:
    def __init__(self):
        self.problemimgUrl = "img/problem.png" # 验证码问题图片名称
        self.imgpath = "img/"
    # 裁剪图片验证码问题
    def problem(self,im):
        # 12306 图片验证码固定大小为 图片宽度和高度分别是(293, 190)
        x = 118
        y = 0
        w = 293 - x
        h = 30
        im = im.crop((x, y, x + w, y + h))
        im.save(self.problemimgUrl)
        return im

    # 裁剪答案选择,2 * 4 个图裁剪出来 返回图片资源数组
    def choice(self,im):
        # 12306 图片验证码固定大小为 图片宽度和高度分别是(293, 190) 每张答案的图固定大小为 67 * 67
        rets = [];
        w = 67
        h = 67
        for i in range(2):
            x = 5
            if i != 0:
                y = 40 + h + 5
            else:
                y = 40
            for j in range(4):
                if j != 0:
                    x = x + w + 5
                tempimg = im.crop((x, y, x + w, y + h))
                rets.append(tempimg)
        return rets

    # 打开一张图片验证码,获得答案
    def go(self,url):
        # 1.加载图片验证码
        checkimg = Image.open(url)

        # 2.切割验证码图片中的问题并保存
        problemimg = self.problem(checkimg)
        problemimg.save(self.problemimgUrl)

        # 3.识别提问
        bApiocr = BApiOcr()
        retOcr = bApiocr.ocr(self.problemimgUrl)

        # 3.切割答案图片并保存
        choiceimgs = self.choice(checkimg)
        for i in range(8):
            choiceimgs[i].save(self.imgpath + str(i) + ".png")

        # 4.识别每张图片的名称
        bApiClassify = BApiClassify()
        answers = []
        print "问题是：" + retOcr
        for i in range(8):
            retClassify = bApiClassify.classify("img/" + str(i) + ".png")
            answers.append(retClassify)
            print "选择【" + str(i + 1) + "】可能是"
            for j in retClassify:
                print "root:" + j.get("root") + ",keyword:" + j.get("keyword") + ",可信度：" + str(j.get("score"))

        # 5.匹配答案
        matching = Matching()
        answerStr = matching.go(retOcr, answers)
        return answerStr