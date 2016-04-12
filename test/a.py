# -*- coding: utf-8 -*-
#! /usr/bin/env python
import urllib2
# import urllib
# url= "http://www.ccgp.gov.cn/json/bid"
# req = urllib2.Request(url)
# data={"bid_time":"0",
#     "bid_type":"",
#     "method":"areaBid",
#     "pagenum":"1",
#     "pagesize":"13",
#     "pin_mu":"",
#     "zone_id":"610000"}
# data = urllib.urlencode(data)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#
# html = opener.open(req,data)
#
#
# print html.read()
#
#
print urllib2.urlopen("http://www.ccgp.gov.cn/cggg/zygg/index.htm").read()