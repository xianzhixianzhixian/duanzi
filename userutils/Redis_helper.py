#!/usr/bin/python
#coding=utf-8
#使用python操作redis数据库工具类
#yufeng on 2018/3/21

import redis

#本例中用到了Redis中的String，所以工具类仅针对String
#key--> author , value--> context:startnums:commentnums
class Redis_helper:

    conn=None

    #获得Redis连接,单例
    @staticmethod
    def getConnection():
        if Redis_helper.conn==None:
            Redis_helper.conn=redis.Redis(host='127.0.0.1',port=6379,db=0)
        else:
            return Redis_helper.conn

    #对Redis进行插入操作
    @staticmethod
    def insertRedis(key,value):
        connection=Redis_helper.getConnection()
        connection.set(key,value)

    #获得某个key对应的value
    @staticmethod
    def getValue(key):
        connection=Redis_helper.getConnection()
        return connection.get(key)