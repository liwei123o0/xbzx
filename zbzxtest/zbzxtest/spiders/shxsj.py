# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Spidershxsj(CrawlSpider):

    name = 'shxsj'
    allowed_domains = ['shxsj']
    start_urls = []

    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))
    for i in xrange(1,179,1):
        start_urls.append("http://www.shxsj.com/lists.php?page=%s&menuid=107&catid=75"%i)
    def parse(self, response):
        sel = scrapy.Selector(response)
        print response.body
        for i in xrange(1,len(sel.xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[1]/td[2]/a")),2):
            title =  sel.xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[2]/a/text()"%i).extract()
            print title