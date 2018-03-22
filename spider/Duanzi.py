#!/usr/bin/python
#coding=utf-8
#段子实体类
#yufeng on 2018/3/22

class Duanzi(object):
    __id=0 #id
    __author='' #作者
    __context='' #主内容
    __startnums='' #点赞数
    __cnotentnums='' #评论数

    def getId(self):
        return id

    def setId(self,id):
        self.__id=id

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author

    def getContext(self):
        return self.__context

    def setContext(self, context):
        self.__context = context

    def getStartnums(self):
        return self.__startnums

    def setStartnums(self, startnums):
        self.__startnums = startnums

    def getCnotentnums(self):
        return self.__cnotentnums

    def setCnotentnums(self, cnotentnums):
        self.__cnotentnums = cnotentnums