# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy import FormRequest
from scrapy.spiders import CrawlSpider,Rule
from zbzxtest.items import Item12312
from scrapy.linkextractors import LinkExtractor
import MySQLdb

class KeywordSpider(CrawlSpider):
    name = '12312search'
    allowed_domains = ['12312.gov.cn']
    start_urls = ['http://bcp.12312.gov.cn/ratingList']

    # conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    # cur  =conn.cursor()

    # def sqlkeyword(self):
    #     self.cur.execute("SELECT gszc FROM test.keywords WHERE COUNTINT=0 LIMIT 5000")
    #     keywords = self.cur.fetchall()
    #     return keywords

    def start_requests(self):
        # self.cur.execute("SELECT gszc FROM test.keywords WHERE COUNTINT=0 LIMIT 1000")
        # self.keywords = self.cur.fetchall()
        #请求之前POST请求获取验证号
        self.zsbh = []
        # print len(self.keywords)
        self.keywords=[u'陕西',u'西安',u'咸阳',u'汉中',u'宝鸡',u'榆林',u'安康',u'铜川',u'商洛',u'渭南']
        for self.keyword in self.keywords:
            print self.keyword
            self.zsbh.append(self.keyword)
            yield FormRequest("http://bcp.12312.gov.cn/ratingList",
                                formdata={'cne':'','cri':'','en':self.keyword,'id1':'',
                                          'id2':'','in':'','oc':'',
                                          'x':'22','y':'12'},
                                callback=self.post_html)
    def post_html(self,response):
        #抓取跟进连接
        sel = scrapy.Selector(response)
        # try:
        urls = sel.xpath("(//li[@class='pj_tablelist8'])/a/@href").extract()
        for url in urls:
            print "url:%s"%url
        # if len(url)==0:
        #     print u"查询不到！"
        #     # for bh in self.zsbh:
        #     #     print "#################post_html#######if#############"
        #     #     print bh,len(self.zsbh)
        #     #     self.cur.execute("UPDATE test.keywords SET COUNTINT =99999 WHERE gszc='%s'"%bh)
        #     #     self.conn.commit()
        #     yield scrapy.Request(response.url,callback=self.parse_item)
        # else:
        #     print u"查询成功！"
        #     print "#################post_html#######else#############"
        #     print url
            print "http://bcp.12312.gov.cn%s"%url
            url = "http://bcp.12312.gov.cn%s"%url
            yield scrapy.Request(url,callback=self.parse_item)
        # except:
        #     self.cur.execute("UPDATE test.keywords SET COUNTINT =99999 WHERE gszc='%s'"%self.keyword)
        #     self.conn.commit()
        #     yield scrapy.Request(response.url,callback=self.parse_item)
    def parse_item(self, response):
        #解析内容
        print "############parse_item#############"
        try:
            print "############parse_item#######try######"
            # print response.url
            item = Item12312()
            sel = scrapy.Selector(response)
            name = sel.xpath("//div[@class='pj_contitle']/span/text()").extract()[0]
            xydj = sel.xpath("(//div[@class='pj_term_resultcon']//li)[1]/span/text()").extract()[0]
            zsbh = sel.xpath("(//div[@class='pj_term_resultcon']//li)[3]/span/text()").extract()[0]
            zsrq = sel.xpath("(//div[@class='pj_term_resultcon']//li)[5]/span/text()").extract()[0]
            yxqz = sel.xpath("(//div[@class='pj_term_resultcon']//li)[7]/span/text()").extract()[0]
            bfdw = sel.xpath("(//div[@class='pj_term_resultcon']//li)[9]//text()").extract()[0]
            zsdz = response.url
            item['name'] = name
            item['xydj'] = xydj
            item['zsbh'] = zsbh
            item['zsrq'] = zsrq
            item['yxqz'] = yxqz
            item['bfdw'] = bfdw
            item['zsdz'] = zsdz
            return item
            # self.cur.execute("UPDATE test.keywords SET COUNTINT += 1 WHERE keyword='%s'"%self.keyword)
            # self.conn.commit()
        except:
            pass
            # self.cur.close()
            # self.conn.close()