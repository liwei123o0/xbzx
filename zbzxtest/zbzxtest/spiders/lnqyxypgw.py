# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from zbzxtest.items import Itemlnqyxypgw
from scrapy.linkextractors import LinkExtractor
class Spiderlnqyxypgw(CrawlSpider):

    name = 'lnqyxypgw'
    allowed_domains = ['lnqyxypgw.com']
    start_urls = ['http://www.lnqyxypgw.com/sx.asp?page=1',
                  'http://www.lnqyxypgw.com/sx.asp?page=2',
                  'http://www.lnqyxypgw.com/sx.asp?page=3',
                  'http://www.lnqyxypgw.com/sx.asp?page=4',
                  'http://www.lnqyxypgw.com/sx.asp?page=5',
                  'http://www.lnqyxypgw.com/sx.asp?page=6',
                  'http://www.lnqyxypgw.com/sx.asp?page=7',
                  'http://www.lnqyxypgw.com/sx.asp?page=8',
                  'http://www.lnqyxypgw.com/sx.asp?page=9',
                  'http://www.lnqyxypgw.com/sx.asp?page=10'
                  ]
    rules = (
        # Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
             Rule(LinkExtractor(restrict_xpaths=("//td[@width='598']/a")),follow=False,callback='parse_item'),)

    def parse_item(self, response):
        item = Itemlnqyxypgw()
        sel = scrapy.Selector(response)
        item['name'] =  "".join(sel.xpath("//a[@class='a3']/text()").extract())
        item['sxtype'] = "".join(sel.xpath("//table[@id='tableData']//tr[2]/td[1]/text()").extract())
        item['bsdw'] = "".join(sel.xpath("//table[@id='tableData']//tr[3]/td[1]/text()").extract())
        item['uptime'] = "".join(sel.xpath("//table[@id='tableData']//tr[3]/td[2]/text()").extract())
        item['zzjgdm'] = "".join(sel.xpath("//table[@id='tableData']//tr[4]/td[2]/text()").extract())
        item['fr'] =  "".join(sel.xpath("//table[@id='tableData']//tr[4]/td[4]/text()").extract())
        item['zcd'] =  "".join(sel.xpath("//table[@id='tableData']//tr[5]/td[2]/text()").extract())
        item['hmd'] =  "".join(sel.xpath("//table[@id='tableData']//tr[5]/td[4]/text()").extract())
        item['url'] = response.url

        return item
