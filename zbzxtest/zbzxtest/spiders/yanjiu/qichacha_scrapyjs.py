# -*- coding: utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy_splash import SplashRequest
from lxml import etree
from scrapy import Selector

class test(scrapy.Spider):

    name = 'qichachajs'

    start_urls = ['http://www.qichacha.com/gongsi?&p=2']

    # for i in xrange(1,500):
    #     start_urls.append("http://www.qichacha.com/gongsi?&p=%s"%i)

    script = \
        """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return {
                url = splash:url(),
                html = splash:html(),
                png = splash:png(),
            }
        end
        """

    #添加cookie
    cookies = {
        'PHPSESSID': '2qqrgo3l7422nsngp40ft7hdf4',
        'think_language': 'zh-cn',
        'pspt': '%7B%22id%22%3A%22250448%22%2C%22pswd%22%3A%228835d2c1351d221b4ab016fbf9e8253f%22%2C%22_code%22%3A%228de0336e04693a20a88a0756a0ff537b%22%7D',
        'td_cookie': '18446744070600212347',
        'SERVERID': 'b7e4e7feacd29b9704e39cfdfe62aefc|1461308942|1461303588',
        'CNZZDATA1254842228': '1609020305-1461302633-%7C1461308490'
        }

    # rules = (Rule(LinkExtractor(restrict_xpaths="(//section[@id='searchlist']/a)[1]"),
    #               follow=False,
    #               callback='parse_item'),)

    def start_requests(self):
        for url in self.start_urls:
            yield  SplashRequest(url,cookies=self.cookies,meta={
                'splash':{
                    'args':{'lua_source':self.script,'url':'http://www.qichacha.com'},
                    'endpoint':'execute',
                }
            })

    def parse(self, response):
        import json
        data = json.loads(response.body)
        with open('png.html','wb')as w:
            w.write(data['html'])

    # def parse_item(self,response):
        # data = response.body
        # print data['html']