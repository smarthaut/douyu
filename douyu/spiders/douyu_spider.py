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
        print('name:'+data[1]['nickname'])
        print('url:'+data[1]['vertical_src'])
        item = DouyuSpiderItem()
        item['name'] = str(data[1]['nickname'])
        item['imageUrls'] = str(data[1]['vertical_src'])
        return item

