#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

def fetch_kxdaili():
    proxyes = []

    url = "http://www.ip181.com/"
    soup = BeautifulSoup(urllib2.urlopen(url).read(),'lxml')
    table = soup.find("table")
    trs = table.find_all("tr")
    for i in range(1, len(trs)):
        tds = trs[i].find_all("td")
        ip = tds[0].text
        port = tds[1].text
        latency = tds[4].text[:-2]
        if float(latency) < 1:
            proxyes.append("%s:%s" % (ip, port))

    return proxyes
