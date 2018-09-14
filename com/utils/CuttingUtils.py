#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CuttingUtils.py
# @Author: Feng
# @Date  : 2018/9/14
# @User  : tanjun
# @Desc  : 裁剪验证码图片并保存工具类
from PIL import Image

from com.config.Config import Config


class CuttingUtils:
    # 裁剪图片验证码问题
    def problem(self,im):
        # http12306 图片验证码固定大小为 图片宽度和高度分别是(293, 190)
        x = 118
        y = 0
        w = 293 - x
        h = 30
        im = im.crop((x, y, x + w, y + h))
        im.save(Config.localproblemimgUrl)
        return im

    # 裁剪答案选择,2 * 4 个图裁剪出来 返回图片资源数组
    def choice(self,im):
        # http12306 图片验证码固定大小为 图片宽度和高度分别是(293, 190) 每张答案的图固定大小为 67 * 67
        index = 1;
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
                tempimg.save(Config.localimgpath + str(index) + Config.imgSuffix)
                index = index + 1
        return rets

    # 裁剪验证码图片
    def go(self):
       im = Image.open(Config.localCheckImg)
       self.problem(im)
       self.choice(im)