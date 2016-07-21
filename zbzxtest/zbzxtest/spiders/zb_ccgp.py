# -*- coding: utf-8 -*-
#! /usr/bin/env python

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zbzxtest.items import *

import sys
reload(sys)
sys.setdefaultencoding("utf8")

class ccgpSpider(CrawlSpider):

    name = 'ccgp'

    start_urls = []

    for i in xrange(1,105,1):
        start_urls.append('http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index={}&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=7&dbselect=bidx&kw=&start_time=2016%3A04%3A19&end_time=2016%3A07%3A20&timeType=4&displayZone=%E9%99%95%E8%A5%BF%E7%9C%81&zoneId=61%25&pppStatus=&agentName='.format(i))

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='vT-srch-result-list-bid']/li/a")),
             follow=False,callback="parse_item"),
    )


    def parse_item(self, response):

        item =Item_Ccgp()

        sel = Selector(response)
        item['XB_URL'] = response.url
        item['XB_TITLE'] = "".join(sel.xpath("//h2/text()").extract())
        item['XB_CONTENT'] = "".join(sel.xpath("//div[@class='vT_detail_content w760c']//text()").extract())
        item['XB_PUBTIME'] = "".join(sel.xpath("//span[@id='pubTime']/text()").extract())
        item['XB_TYPE'] =u'中标公告'
        item['XB_GROUPNAME'] = u'招标信息'
        item['XB_REGION'] = u'陕西省'
        item['XB_SITENAME'] = u'中国政府采购网'

        return item