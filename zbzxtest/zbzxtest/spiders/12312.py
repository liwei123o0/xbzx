# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zbzxtest.items import *
class Myspider(CrawlSpider):

    name = '12312'
    allowed_domains = ['gov.cn']
    start_urls = ['http://bcp.12312.gov.cn/ratingList']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='pj_search_prev']/a[last()-1]")),follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//li[@class='pj_tablelist8']/a"),),follow=False,callback='parse_item')
    )
    def parse_item(self,response):
        item = ZbzxtestItem()
        sel = Selector(response)
        try:
            item['url'] = response.url
            item['name'] = sel.xpath("//div[@class='pj_contitle']/span/text()").extract()[0]
            item['xy']  = sel.xpath("(//div[@class='pj_term_resultcon']//li)[1]/span/text()").extract()[0]
            item['zsbh'] = sel.xpath("(//div[@class='pj_term_resultcon']//li)[3]/span/text()").extract()[0]
            item['bftime'] = sel.xpath("(//div[@class='pj_term_resultcon']//li)[5]/span/text()").extract()[0]
            item['yxtime'] = sel.xpath("(//div[@class='pj_term_resultcon']//li)[7]/span/text()").extract()[0]
            item['fzdw']    = sel.xpath("(//div[@class='pj_term_resultcon']//li)[9]//text()").extract()[0]
            item['gszch']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[1])[2]/span/text()").extract()[0]
            item['jgdm']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[3])[2]/span/text()").extract()[0]
            item['frdb']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[5])[2]/span/text()").extract()[0]
            item['zczb']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[7])[2]/span/text()").extract()[0]
            item['sshy']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[9])[2]/span/text()").extract()[0]
            item['qywz']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[11])/span/text()").extract()[0]
            item['ssdq']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[13])/span/text()").extract()[0]
            item['yb']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[15])/span/text()").extract()[0]
            item['yydz']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[17])/span/text()").extract()[0]
            item['zyyw']   = sel.xpath("(//div[@class='pj_term_resultcon']//li[19])/span/text()").extract()[0]
        except:
            pass
        return item