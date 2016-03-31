#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy import signals, log
from urlparse import urlparse
import random, re


class ProxyMiddleware(object):

    def __init__(self, crawler):
        self.enabled = False
        self.proxy_list = []
        self.idx = 0
        self.cur = None
        crawler.signals.connect(self.spider_opened, signals.spider_opened)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def spider_opened(self, spider):
        try:
            if hasattr(spider, 'proxy'):
                m = re.match(r'^(http://[.0-9]+:[0-9]+)(,(http://[.0-9]+:[0-9]+))*$', spider.proxy)
                if m:
                    proxy = {
                        'list': spider.proxy.split(','),
                        'rate': 1
                    }
                else:
                    proxy = {
                        'file': spider.proxy,
                        'rate': 1
                    }
            else:
                proxy = {'enabled':False}

            self.enabled = proxy.get('enabled', True)
            if not self.enabled:
                return

            self.rate = proxy.get('rate', 10)

            for i in utils.load_keywords(proxy, msg='proxies'):
                m = re.match(r'^(?P<prot>\S+)(\s+|://)(?P<host>\S+)(\s+|:)(?P<port>\S+)$', i)
                if m:
                    self.proxy_list.append(m.groupdict())
                else:
                    log.msg('drop invalid proxy <{}>'.format(i), log.WARNING)

        except Exception as ex:
            self.enabled = False
            log.msg('cannot load proxies: {}'.format(ex))

    def process_request(self, request, spider):
        if self.proxy_bypass(request) or not (self.enabled and self.proxy_list):
            return
        self.idx += 1
        if (not self.cur) or self.idx>=self.rate:
            self.idx = 0
            proxy = random.choice(self.proxy_list)
            self.cur = '{0[prot]}://{0[host]}:{0[port]}'.format(proxy)
        request.meta['proxy'] = self.cur

    def proxy_bypass(self, request):
        return urlparse(request.url).hostname.startswith('192.168.')