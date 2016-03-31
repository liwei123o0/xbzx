# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import *
class DeepSpiderItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()

#动态运行多个spider
class DeepSpider(CrawlSpider):
    name = "deep"

    def __init__(self,rule):
        self.rule = rule
        self.name = rule.name
        self.allowed_domains = rule.allowed_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        rule_list =[]

        if rule.next_page:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page)))

        rule_list.append(Rule(LinkExtractor(
            allow=[rule.allow_url],
            restrict_xpaths= [rule.extract_from]),
        callback="parse_item"))
        self.rules = tuple(rule_list)
        super(DeepSpider,self).___init__()

    def parse_item(self,response):
        sel = scrapy.Selector(response)
        item = DeepSpiderItem()
        item['url'] = response.url

        name = sel.xpath(self.rule.title_xpath).extract()
        item['name'] = name[0] if name else ""

        content = sel.xpath(self.rule.body_xpath).extract()
        item['content'] = content[0] if content else ""

        return item