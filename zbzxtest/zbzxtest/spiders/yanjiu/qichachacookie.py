# -*- coding: utf-8 -*-
#! /usr/bin/env python
from scrapy.spiders import Spider
from scrapy.http import Request
from chardet import detect

class Qichacha(Spider):
    name = 'qichacha'

    allowed_domains = ['qichacha.com']
    start_urls = ['http://www.qichacha.com']
    #添加cookie
    cookies = {'PHPSESSID': '2qqrgo3l7422nsngp40ft7hdf4',
               'think_language': 'zh-cn',
               'pspt': '%7B%22id%22%3A%22250448%22%2C%22pswd%22%3A%228835d2c1351d221b4ab016fbf9e8253f%22%2C%22_code%22%3A%228de0336e04693a20a88a0756a0ff537b%22%7D',
               'td_cookie': '18446744070600212347',
               'SERVERID': 'b7e4e7feacd29b9704e39cfdfe62aefc|1461308942|1461303588',
               'CNZZDATA1254842228': '1609020305-1461302633-%7C1461308490'}

    def start_requests(self):
        yield Request('http://qichacha.com/firm_XJ_2c5e0460631b00469ecbe944df589f90.shtml',cookies=self.cookies,callback=self.parse_item)

    def parse_item(self, response):
        body =  response.body
        body =  body.decode('utf8')
        with open('qichacha.html','wb')as w:
            w.write(body.encode('utf8'))
        print response.url

