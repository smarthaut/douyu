#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 16:11
# @Author  : huanghe
# @Site    : 
# @File    : douyu_spider.py
# @Software: PyCharm

import scrapy
import json
from douyu.items import DouyuSpiderItem

class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowd_domains = ["http://capi.douyucdn.cn"]

    offset = 20
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.body_as_unicode())["data"]
        for each in data:
            item = DouyuSpiderItem()
            item['name'] = str(each['nickname'])
            item['imageUrls'] = str(each['vertical_src'])
            yield item
        self.offset += 20
        if self.offset <= 200:
            yield scrapy.Request(self.url+str(self.offset),callback = self.parse)
        else:
            return


