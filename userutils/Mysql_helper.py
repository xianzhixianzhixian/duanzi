#!/usr/bin/python
#coding=utf-8
#使用python操作mysql数据库工具类
#yufeng on 2018/3/9

import pymysql
from spider.Duanzi import Duanzi

class Mysql_helper(object):
    #包括数据库的增删改
    @staticmethod
    def update(sql):
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='duanzi', charset='utf8')
        statement = conn.cursor()
        # 查询
        try:
            num = statement.execute(sql)
            conn.commit()
            return num
        except Exception as e:
            conn.rollback()
            print("Exception", e)
        finally:
            statement.close()
            conn.close()

    #包括数据库的查询
    @staticmethod
    def select(sql):
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='duanzi', charset='utf8')
        statement = conn.cursor()
        try:
            statement.execute(sql)
            results = statement.fetchall()
            list = []
            for row in results:
                duanzi= Duanzi()
                id = row[0]
                author = row[1]
                context = row[2]
                startnums = row[3]
                commentnums = row[4]
                duanzi.setId(id)
                duanzi.setAuthor(author)
                duanzi.setContext(context)
                duanzi.setStartnums(startnums)
                duanzi.setCnotentnums(commentnums)
                list.append(duanzi)
            return list
        except Exception as e:
            print("Exception", e)
        finally:
            statement.close()
            conn.close()

    @staticmethod
    def check(username,password):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='duanzi', charset='utf8')
        statement = conn.cursor()
        sql='select id from user where username=\'%s\' and pwssword=\'%s\''%(username,password)
        try:
            statement.execute(sql)
            results = statement.fetchall()
            if results.__len__()!=0:
                return True
            else:
                return False
        except Exception as e:
            print("Exception", e)
            return False
        finally:
            statement.close()
            conn.close()
