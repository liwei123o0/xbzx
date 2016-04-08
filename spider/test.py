# -*- coding: utf-8 -*-
#! /usr/bin/env python
import chardet
import urllib2

html = urllib2.urlopen("http://www.bcpcn.com/product/hhbang/63920/index.html").read()
print html