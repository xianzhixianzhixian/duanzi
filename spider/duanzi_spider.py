#!/usr/bin/python
#coding=utf-8
#使用python操作mysql数据库工具类
#yufeng on 2018/3/21

import os
import requests
from lxml import etree
from userutils.Mysql_helper import Mysql_helper

# 段子爬虫
class QSBK:
    # 初始化方法，定义变量
    def __init__(self):
        self.pageIndex = 1
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
        }
        self.enable = False

    # 返回页面的div_list
    def getHtmlDivList(self, pageIndex):
        pageUrl = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        html = requests.get(url=pageUrl, headers=self.headers).text
        selector = etree.HTML(html)
        divList = selector.xpath('//div[@id="content-left"]/div')
        return divList

    # 获取文本中要截取的元素
    def getHtmlItems(self, divList):

        items = []

        for div in divList:
            item = []
            # 发布人
            name = div.xpath('.//h2/text()')[0].replace("\n", "")
            item.append(name)

            # 内容(阅读全文)
            contentForAll = div.xpath('.//div[@class="content"]/span[@class="contentForAll"]')
            if contentForAll:
                contentForAllHref = div.xpath('.//a[@class="contentHerf"]/@href')[0]
                contentForAllHref = "https://www.qiushibaike.com" + contentForAllHref
                contentForAllHrefPage = requests.get(url=contentForAllHref).text
                selector2 = etree.HTML(contentForAllHrefPage)
                content = selector2.xpath('//div[@class="content"]/text()')
                content = "".join(content)
                content = content.replace("\n", "")
            else:
                content = div.xpath('.//div[@class="content"]/span/text()')
                content = "".join(content)
                content = content.replace("\n", "")
            item.append(content)

            # 点赞数
            love = div.xpath('.//span[@class="stats-vote"]/i[@class="number"]/text()')
            love = love[0]
            item.append(love)

            # 评论人数
            num = div.xpath('.//span[@class="stats-comments"]//i[@class="number"]/text()')
            num = num[0]
            item.append(num)

            items.append(item)

        return items

    # 保存入文本
    def saveItem(self, items):
        f = open('qiushi.txt', "a", encoding='UTF-8')

        for item in items:
            name = item[0]
            content = item[1]
            love = item[2]
            num = item[3]

            # 写入数据库
            sql = 'insert into daunzi(author,context,startnums,commentnums) values(\'%s\',\'%s\',\'%s\',\'%s\')' %(str(name),content,love,num)
            Mysql_helper.update(sql)
        f.close()

    def start(self):
        print("正在读取糗事百科")
        self.enable = True
        while self.enable:
            divList = self.getHtmlDivList(self.pageIndex)
            data = self.getHtmlItems(divList)
            self.saveItem(data)
            print('已保存第%d页的内容' % self.pageIndex)
            self.pageIndex=self.pageIndex+1
            if self.pageIndex>=30:
                break

spider = QSBK()
spider.start()