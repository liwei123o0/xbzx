# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver

#启动火狐配置文件
proxyfile = webdriver.FirefoxProfile()
#代理设置为开启1表示开启,0表示关闭
proxyfile.set_preference('network.proxy.type',1)
#添加代理及端口号
proxyfile.set_preference('network.proxy.http','119.29.111.249')
proxyfile.set_preference('network.proxy.http_port',80)
#添加https的代理及端口号
proxyfile.set_preference('network.proxy.ssl','119.29.111.249')
proxyfile.set_preference('network.proxy.ssl_port',80)
#更新设置
proxyfile.update_preferences()
#启动火狐并加载代理设置
driver = webdriver.Firefox(proxyfile)

