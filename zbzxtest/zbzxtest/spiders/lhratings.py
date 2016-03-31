# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider
from zbzxtest.items import Itemlhratings
class Spiderlhratings(CrawlSpider):

    name = 'lhratings'
    allowed_domains = ['lhratings.com']
    start_urls = ['http://www.lhratings.com/announcement/index.html?type=1',
                  'http://www.lhratings.com/announcement/index.html?type=2',
                  'http://www.lhratings.com/announcement/index.html?type=3',
                  'http://www.lhratings.com/announcement/index.html?type=4'
                  ]
    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))

    def parse(self, response):
        item = Itemlhratings()
        sel = scrapy.Selector(response)
        for i in range(len(sel.xpath("//table[@class='list-table']/tbody//tr"))):
            item['name'] =  sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[2]/a/text()"%(i+1)).extract()[0]
            item['ztjb'] = sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[3]/text()"%(i+1)).extract()[0]
            item['zw'] = sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[4]/text()"%(i+1)).extract()[0]
            item['zxjb'] = sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[5]/text()"%(i+1)).extract()[0]
            item['uptime'] = sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[6]/text()"%(i+1)).extract()[0]
            item['url'] =  sel.xpath("//table[@class='list-table']/tbody//tr[%s]/td[2]/a/@href"%(i+1)).extract()[0]
            yield item
