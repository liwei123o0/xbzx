# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider
from zbzxtest.items import Iitemccxi
import MySQLdb
class Spiderccxi(CrawlSpider):

    name = 'ccxi'
    allowed_domains = ['ccxi.com.cn']
    start_urls = []
    for i in range(1,166,1):
        start_urls.append("http://www.ccxi.com.cn/01-01/NoteList-%s.html"%i)
    # rules = (Rule(LinkExtractor(restrict_xpaths=("//table/tbody//tr/td/a[last()-1]|//a[@class='zq']")),follow=True),
    #          Rule(LinkExtractor(restrict_xpaths=("//a[@class='zq']")),follow=False,callback='parse_item'))
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    def parse(self, response):
        item = Iitemccxi()
        sel = scrapy.Selector(response)

        for i in xrange(len(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr"))):
            item['name'] =  "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[2]//text()"%(i+1)).extract())
            item['pj'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[3]//text()"%(i+1)).extract())
            item['szxpj'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[4]//text()"%(i+1)).extract())
            item['spjsj'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[5]//text()"%(i+1)).extract())
            item['zzxpj'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[6]//text()"%(i+1)).extract())
            item['zpjsj'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[7]//text()"%(i+1)).extract())
            item['url'] = "".join(sel.xpath("//div[@class='qyxx-10']//table[@cellspacing='1']//tr[%s]/td[2]/a/@href"%(i+1)).extract())
            item['url'] = "http://www.ccxi.com.cn%s"%item['url']
            try:
                self.cur.execute(u"INSERT INTO spider.ccxi ("
                                 "url,name,pj,szxpj,spjsj,zzxpj,zpjsj) VALUES "
                                 "('%s','%s','%s','%s','%s','%s','%s')"%(
                                item['url'],item['name'],item['pj'],item['szxpj'],item['spjsj'],item['zzxpj'],
                                item['zpjsj']
                                ))
                self.conn.commit()
            except MySQLdb.Error,e :
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            yield item