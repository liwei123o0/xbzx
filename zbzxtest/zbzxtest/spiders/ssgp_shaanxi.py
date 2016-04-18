# -*- coding: utf-8 -*-
#! /usr/bin/env python

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import  Selector
class ccgpShanxiSpider(CrawlSpider):

    name = 'ccgpshaanxi'
    allowed_domains = ['ccgp-shaanxi.gov.cn']
    start_urls = ['http://www.ccgp-shaanxi.gov.cn/zbAllDq_view.jsp?ClassName=C0001&pages=5']
    # for i in xrange(1,100,1):
    #     start_urls.append("http://www.ccgp-shaanxi.gov.cn/zbAllDq_view.jsp?ClassName=C0001&pages=%s"%i)

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=("//form[@name='formBean']//a[last()-1]"))),
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='b']")),follow=False,callback='parse_item')
    ,)

    def parse_item(self, response):
        sel = Selector(response)
        title = sel.xpath("//h2/text()").extract()[0]
        print title

