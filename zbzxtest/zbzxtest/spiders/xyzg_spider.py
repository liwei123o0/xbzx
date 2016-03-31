# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zbzxtest.items import *
class Myspider(CrawlSpider):

    name = 'ce9000'
    allowed_domains = ['ce9000.com']
    start_urls = ['http://www.ce9000.com/xyqy21.asp']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("(//table)[3]//tr[last()]//a[last()-1] |　//td[@class='lmcss']/a")),follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//table)[3]//tr[position()>=1 and position()<last()-1]//a"),),follow=False,callback='parse_item')
    )
    def parse_item(self,response):
        item = ZbzxtestItem()
        sel = Selector(response)
        item['url'] = response.url
        item['name'] = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[1]//text()").extract()[0]
        item['gjxym']  = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[2]//text()").extract()[0]
        item['rzjg'] = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[3]//text()").extract()[0]
        item['zs'] = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[4]//text()").extract()[0]
        item['zch'] = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[5]//text()").extract()[0]
        item['bz']    = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[6]//text()").extract()[0]
        item['yxrq']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[7]//text()").extract()[0]
        item['zszt']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[8]//text()").extract()[0]
        item['frdb']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[9]//text()").extract()[0]
        item['zch']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[11]//text()").extract()[0]
        item['zcdz']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[12]//text()").extract()[0]
        item['fr']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[13]//text()").extract()[0]
        item['djjg']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[14]//text()").extract()[0]
        item['jjfw']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[15]//text()").extract()[0]
        item['lxdh']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[17]//text()").extract()[0]
        item['xyjf']   = sel.xpath("(//table[@class='qylbnl']//tr/td[2])[22]//text()").extract()[0]
        return item