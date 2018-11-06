#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ShowTickeList.py
# @Author: Feng
# @Date  : 2018/9/19
# @User  : tanjun
# @Desc  : 打印余票功能
class ShowTickeList:

    def showList(self,tickeList):
        for ticke in tickeList:
            ticke = ticke.encode("utf8")
            cols = ticke.split("|")
            if cols[3][0:1] == "G":  # 只查询高铁
                print "------------------------------------------------------"
                print "日期:" + cols[13] + \
                      ",车次:" + cols[3] + \
                      ",开车时间:" + cols[8] + \
                      ",到达时间:" + cols[9] + \
                      ",耗时:" + cols[10] + \
                      ",是否有票" + cols[11] + \
                      ",二等座:" + cols[30] + \
                      ",一等座:" + cols[31] + \
                      ",商务座/特等座:" + cols[32] + \
                      ",无座:" + cols[26] + \
                      ",ticketId:" + cols[0]
