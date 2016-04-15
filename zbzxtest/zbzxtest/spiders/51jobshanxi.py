# -*- coding: utf-8 -*-
#! /usr/bin/env python
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
from zbzxtest.items import ItemJob51SAX
class Job51Spider(CrawlSpider):
    name = '51jobsax'
    allowed_domains = ['51job.com']
    start_urls = []
    for i in range(1,100):
        url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=210000&curr_page=%s"%i
        start_urls.append(url)

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='dw_table']//div[@class='el']/p/a")),
             follow=False,
             callback='parse_item'),
    )

    def parse_item(self, response):

        sel = Selector(response)
        item = ItemJob51SAX()
        item['url'] = response.url
        item['job'] = sel.xpath("//h1/@title").extract()[0]
        item['name'] = sel.xpath("//p[@class='cname']/a/@title").extract()[0]
        item['address'] = sel.xpath("//span[@class='lname']/text()").extract()[0]
        item['pay']     = sel.xpath("//div[@class='cn']/strong/text()").extract()[0]
        item['pub_date'] = "".join(sel.xpath("(//span[@class='sp4'])[last()]/text()").extract())
        item['pub_date'] = "2016-"+re.sub(u"发.*","",item['pub_date'])
        item['contact']  = "".join(sel.xpath("//p[@class='fp']/text()").extract())
        item['contact'] = re.sub(r"\s+","",item['contact'])
        # content  = sel.xpath("//div[@class='tmsg inbox']//text()").extract()[0]
        # content = re.sub(r"\s+","",content)
        # print "##########################"
        # print "url:%s"%item['url']
        # print "job:%s"%item['job']
        # print "name:%s"%item['name']
        # print "address:%s"%item['address']
        # print "pay:%s"%item['pay']
        # print "pub_date:%s"%item['pub_date']
        # print "contact:%s"%item['contact']
        return item
        # print "content:%s"%content