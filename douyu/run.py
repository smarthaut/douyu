#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 16:20
# @Author  : huanghe
# @Site    : 
# @File    : run.py
# @Software: PyCharm
from scrapy import cmdline

cmdline.execute('scrapy crawl douyu'.split())