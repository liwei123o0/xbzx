# -*- coding: utf-8 -*-
#! /usr/bin/env python
from scrapy import Spider,Request,Selector
import time
from zbzxtest.items import Item_Gsxx_XJ
import re
import MySQLdb
class Gsxx_XJ(Spider):
    name = 'xinjiang'

    start_urls=[]

    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()

    for i in range(6501000000000001,6501000000099991,1):
         start_urls.append("http://gsxt.xjaic.gov.cn:7001/ztxy.do?method=qyInfo&maent.pripid=%s&czmk=czmk11&random="%i)

    def start_requests(self):
        for url in self.start_urls:
            yield Request("".join(url+"%s"%int(time.time())))

    def parse(self, response):
        item =Item_Gsxx_XJ()
        sel = Selector(response)
        djxx = "".join(sel.xpath("(//table[@class='detailsList'])[1]//tr[position()>1]//text()").extract())
        djxx = re.sub("\\xa0","",djxx)
        item['url'] =  response.url
        item['name'] =  "".join(sel.xpath("(//table[@class='detailsList'])[1]//tr[2]/td[2]/text()").extract())
        item['xym'] =  "".join(sel.xpath("(//table[@class='detailsList'])[1]//tr[2]/td[1]/text()").extract())
        item['gstype'] =  "".join(sel.xpath("(//table[@class='detailsList'])[1]//tr[3]/td[1]/text()").extract())
        item['fr'] =  "".join(sel.xpath("(//table[@class='detailsList'])[1]//tr[3]/td[2]/text()").extract())
        # print item['url']
        # print item['name']
        # print item['xym']
        # print item['gstype']
        # print item['fr']
        # yycs =  re.findall(u"(?<=营业场所\r\n).*",djxx,re.DOTALL)
        yycs =  "".join(re.findall(u"(?<=住所\r\n).*",djxx,re.DOTALL))
        item['yycs'] = re.sub("\s+","",yycs.split("\r\n")[1])
        # print item['yycs']
        zczb =  "".join(re.findall(u"(?<=注册资本).*",djxx,re.DOTALL))
        item['zczb'] = re.sub("\s+","",zczb.split("\r\n")[2])
        # print item['zczb']
        cltime =  "".join(re.findall(u"(?<=成立日期).*",djxx,re.DOTALL))
        item['cltime'] = re.sub("\s+","",cltime.split("\r\n")[1])
        # print item['cltime']

        yyqx =  "".join(re.findall(u"(?<=营业期限自).*",djxx,re.DOTALL))
        item['yyqx'] = re.sub("\s+","",yyqx.split("\r\n")[1])
        # print item['yyqx']
        try:
            yyqxz =  "".join(re.findall(u"(?<=营业期限至).*",djxx,re.DOTALL))
            item['yyqxz'] = re.sub("\s+","",yyqxz.split("\r\n")[1])
            # print item['yyqxz']
        except:
            item['yyqxz'] = ""
        yywf =  "".join(re.findall(u"(?<=经营范围).*",djxx,re.DOTALL))
        item['yywf'] = re.sub("\s+","",yywf.split("\r\n")[1])
        # print item['jywf']

        djjg =  "".join(re.findall(u"(?<=登记机关).*",djxx,re.DOTALL))
        item['djjg'] = re.sub("\s+","",djjg.split("\r\n")[1])
        # print item['djjg']

        hzrq =  "".join(re.findall(u"(?<=核准日期).*",djxx,re.DOTALL))
        item['hzrq'] = re.sub("\s+","",hzrq.split("\r\n")[1])
        # print item['hzrq']

        djzt =  "".join(re.findall(u"(?<=登记状态).*",djxx,re.DOTALL))
        item['djzt'] = djzt.split("\t")[3]
        # print item['djzt']



        return item