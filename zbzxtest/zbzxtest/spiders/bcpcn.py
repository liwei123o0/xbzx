# -*- coding: utf-8 -*-
#! /usr/bin/env python
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from zbzxtest.items import ItemBcpcn
import MySQLdb
class bcpcnSpider(CrawlSpider):
    name = 'bcpcn'
    allowed_domains = ['bcpcn.com']

    start_urls = []
    for i in xrange(1,481,1):
        start_urls.append("http://www.bcpcn.com/gfthhbanglist?&sid=141&rn=50&pn=%s"%i)

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//span[@class='width_260']/a")),
             follow=False,
             callback='parse_item'),
    )
    # conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    # cur  =conn.cursor()
    def parse_item(self, response):
        sel = Selector(response)
        item = ItemBcpcn()
        item['url'] = response.url
        item['name'] = "".join(sel.xpath("//li[@class='bang_tit heibang_tit']/text()").extract())
        item['cftype'] =  "".join(sel.xpath("//div[@class='hongbang_body heibang_body']//li[3]/text()").extract())
        item['cftype'] = item['cftype'].replace("\r\n","")
        item['cftime'] =  sel.xpath("//div[@class='hongbang_body heibang_body']//li[4]/text()").extract()[0]
        item['cftime'] = item['cftime'].replace("\r\n","")
        item['cfjg'] =  sel.xpath("//div[@class='hongbang_body heibang_body']//li[5]/text()").extract()[0]
        item['cfjg'] = item['cfjg'].replace("\r\n","")
        item['cftime'] = item['cftime'].encode("GB18030")
        item['cfjg'] = item['cfjg'].encode("GB18030")
        return item
        # try:
        #     self.cur.execute(u"INSERT INTO spider.bcpcn ("
        #                          "url,name,cftype,cftime,cfjg) VALUES "
        #                          "('%s','%s','%s','%s','%s')"%(
        #                         item['url'],item['name'],item['cftype'],item['cftime'],item['cfjg']
        #                         ))
        #     self.conn.commit()
        # except MySQLdb.Error,e :
        #     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        # print "#####################################"
        # print item['url']
        # print item['name']
        # print item['cftype']
        # print type(item['cftime'])
        # print type(item['cftime'].encode("GB18030"))
        # print item['cfjg'].encode("GB18030")
        # print cftime.encode("GB18030")
        # print cfjg.encode("GB18030")
