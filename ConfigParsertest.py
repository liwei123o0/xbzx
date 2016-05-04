# -*- coding: utf-8 -*-
#! /usr/bin/env python

#读取INI配置文件
import ConfigParser

conf = ConfigParser.ConfigParser()

readtest = conf.read('test.json')
print readtest

sectiontest = conf.sections()
print sectiontest

start_urls =  conf.get('spider','start_urls').split(',')
print start_urls
