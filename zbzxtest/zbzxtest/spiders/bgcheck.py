# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from zbzxtest.items import Itembgcheck
class Spiderbgcheck(scrapy.Spider):

    name = 'bgcheck'
    allowed_domains = ['bgcheck.cn']
    start_urls = ['http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E8%A5%BF%E5%AE%89',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E5%92%B8%E9%98%B3',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E6%B1%89%E4%B8%AD',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E5%AE%9D%E9%B8%A1',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E6%B8%AD%E5%8D%97',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E5%BB%B6%E5%AE%89',
                  'http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%E5%AE%89%E5%BA%B7']

    def parse(self, response):
        sel = scrapy.Selector(response)
        item = Itembgcheck()
        for i in range(len(sel.xpath("//div[@id='content1']/ul[position()<=last()-1]"))):
            item['name'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/a[1]//text()"%(i+1)).extract()
            item['xydj'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[1]/text()"%(i+1)).extract()
            item['xypm'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/span[1]//text()"%(i+1)).extract()
            item['xyzk'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/span[2]//text()"%(i+1)).extract()
            item['sshy'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[2]//text()"%(i+1)).extract()
            item['szdq'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[3]//text()"%(i+1)).extract()
            item['gsdz'] = sel.xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/a[1]/@href"%(i+1)).extract()[0]

            item['name'] = "".join(item['name'])
            item['xydj'] = "".join(item['xydj'])
            item['xypm'] = "".join(item['xypm'])
            item['xyzk'] = "".join(item['xyzk'])
            item['sshy'] = "".join(item['sshy'])
            item['szdq'] = "".join(item['szdq'])
            item['gsdz'] = "http://www.bgcheck.cn%s"%(item['gsdz'])

            print item['name']
            print item['xydj']
            print item['xypm']
            print item['xyzk']
            print item['sshy']
            print item['szdq']
            print item['gsdz']

            yield item