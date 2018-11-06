#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MysqlUtils.py
# @Author: Feng
# @Date  : 2018/7/4
# @User  : tanjun
# @Desc  : 操作mysql
import pymysql.cursors
from pymysql import IntegrityError

from com.config.Config import Config


class MysqlUtils:
    # 获取一个连接 不是自动提交 需要手动管理事务
    def getConnect(self):
        return pymysql.connect(**Config.mysqlconfig)

    # 添加需要执行的 无需返回的sql数组,将把它们设置成同一个事务  参数是 [{"sql":"","param":()}]
    def addSql(self,sqls):
        try:
            connection = self.getConnect()
            with connection.cursor() as cursor:
                for sql in sqls:
                    try:
                        cursor.execute(sql.get("sql"),sql.get("param"))
                    except IntegrityError:
                        print "添加重复图片数据,无视这个异常"
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
        finally:
            connection.close()

    #查询数据
    def querySql(self,sql,param):
        connection = self.getConnect()
        with connection.cursor() as cursor:
            cursor.execute(sql,param)
            return cursor

