# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Spidershxsj(CrawlSpider):

    name = 'shxsj'
    allowed_domains = ['shxsj.com']
    start_urls = ['http://www.shxsj.com/lists.php?page=1&menuid=107&catid=75']

    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))

    def parse(self, response):
        sel = scrapy.Selector(response)
        title =  sel.xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[1]/td[2]/a/@title").extract()
        print sel.xpath("//text()").extract()
        print title
        # code = chardet.detect(str(title))
        # print code