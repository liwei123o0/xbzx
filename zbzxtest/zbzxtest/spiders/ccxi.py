# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider
from zbzxtest.items import Iitemccxi
class Spiderccxi(CrawlSpider):

    name = 'ccxi'
    allowed_domains = ['ccxi.com.cn']
    start_urls = ['http://www.ccxi.com.cn/01-01/NoteList.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-2.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-3.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-4.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-5.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-6.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-7.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-8.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-9.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-10.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-11.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-12.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-13.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-14.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-15.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-16.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-17.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-18.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-19.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-20.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-21.html',
                  'http://www.ccxi.com.cn/01-01/NoteList-22.html'
                  ]
    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))

    def parse(self, response):
        item = Iitemccxi()
        sel = scrapy.Selector(response)
        for i in range(len(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr"))):
            item['name'] =  sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[2]//text()"%(i+1)).extract()[0]
            item['pj'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[3]//text()"%(i+1)).extract()[0]
            item['szxpj'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[4]//text()"%(i+1)).extract()[0]
            item['spjsj'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[5]//text()"%(i+1)).extract()[0]
            item['zzxpj'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[6]//text()"%(i+1)).extract()[0]
            item['zpjsj'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[7]//text()"%(i+1)).extract()[0]
            item['url'] = sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[2]/a/@href"%(i+1)).extract()[0]
            item['url'] = "http://www.ccxi.com.cn%s"%item['url']
            yield item
