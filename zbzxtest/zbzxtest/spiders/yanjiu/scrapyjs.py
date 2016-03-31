# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from zbzxtest.items import JrttItem
import json
from lxml import etree
from scrapy import Selector

class test(scrapy.Spider):
    name = 'test'
    start_urls = ['http://toutiao.com/']

    def start_requests(self):
        script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return {
                html = splash:html(),
            }
        end
                """
        for url in self.start_urls:
            yield scrapy.Request(url,self.parse,meta={
                'splash':{
                    'args':{'lua_source':script,'url':url},
                    'endpoint':'execute',
                }
            })
    def parse(self, response):
        item = JrttItem()
        data = json.loads(response.body_as_unicode())
        html = data['html']
        sel = etree.HTML(html)
        content = sel.xpath("(//a[@class='link title'])[1]/text()")[0]
        item['content'] = content
        return item