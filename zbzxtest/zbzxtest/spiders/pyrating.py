# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from zbzxtest.items import Itempyrating
class Spiderccxi(CrawlSpider):
    name = 'pyrating'
    allowed_domains = ['pyrating.cn']
    start_urls = ['http://www.pyrating.cn/zh-cn/statement/qiyezhaiquanpingji',
                  'http://www.pyrating.cn/zh-cn/statement/gongsizhaiquanpingji',
                  'http://www.pyrating.cn/zh-cn/statement/jihezhaiquanpingji',
                  'http://www.pyrating.cn/zh-cn/statement/zhutipingji'
                  ]
    rules = (
        Rule(
            LinkExtractor(
            restrict_xpaths=("//td[@class='text_left']/a"),
            ),
            follow=False,
            callback='parse_item')
        ,)
    def parse_item(self, response):
        item = Itempyrating()
        sel = scrapy.Selector(response)
        item['url'] = response.url
        item['name'] =  "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[2]/td[2]//text()").extract())
        item['name'] = item['name'].replace("\r\n","").replace("                                        ","")
        item['qytype'] =  "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[2]/td[1]//text()").extract())
        item['ztjb'] = "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[6]/td[1]/text()").extract())
        item['ztjb'] = item['ztjb'].replace("\r\n","")
        item['zjjb'] = "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[6]/td[2]/text()").extract())
        item['zjjb'] = item['zjjb'].replace("\r\n","")
        item['pjzw'] = "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[7]/td[1]/text()").extract())
        item['pjnd'] = "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[7]/td[2]/text()").extract())
        item['pjsj'] = "".join(sel.xpath("//div[@class='table_list table_list_3 mb_2']//tr[9]/td[1]/text()").extract())
        return item
