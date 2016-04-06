# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider
from zbzxtest.items import Itemlhratings
import MySQLdb

class Spiderlhratings(CrawlSpider):

    name = 'lhratings'
    allowed_domains = ['lhratings.com']
    start_urls = [
                  'http://www.lhratings.com/announcement/index.html?type=2&page=1',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=2',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=3',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=4',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=5',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=6',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=7',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=8',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=9',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=10',
                  'http://www.lhratings.com/announcement/index.html?type=2&page=11',
                  ]
    # for i in xrange(1,163,1):
    #     start_urls.append("http://www.lhratings.com/announcement/index.html?type=1&page=%s"%i)
    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
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
            try:
                self.cur.execute(u"INSERT INTO spider.lhratings ("
                                 "url,name,ztjb,zw,zxjb,uptime) VALUES "
                                 "('%s','%s','%s','%s','%s','%s')"%(
                                item['url'],item['name'],item['ztjb'],item['zw'],item['zxjb'],item['uptime']
                                ))
                self.conn.commit()
            except MySQLdb.Error,e :
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

            yield item
