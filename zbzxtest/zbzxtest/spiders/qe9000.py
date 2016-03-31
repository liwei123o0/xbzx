# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import chardet
class Spiderqe9000(CrawlSpider):

    name = 'qe9000'
    allowed_domains = ['qe9000.com']
    start_urls = ['http://www.qe9000.com/CertificateList.asp?cid=1']

    rules = (Rule(LinkExtractor(restrict_xpaths=("//div[@id='fy1']/b[last()-1]/a")),follow=True),
             Rule(LinkExtractor(restrict_xpaths=("//div[@id='certxwlb']//li/a")),follow=False,callback='parse_item'))

    def parse_item(self, response):
        sel = scrapy.Selector(response)
        title =  sel.xpath("//p[@class='di'][last()]//text()").extract()[0]
        print title
        # code = chardet.detect(str(title))
        # print code