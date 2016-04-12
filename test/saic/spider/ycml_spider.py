# -*- coding: utf-8 -*-
#! /usr/bin/env python
from  selenium import webdriver

def ycmlspider(url):

    driver = webdriver.Firefox()
    driver.get(url)
    title = driver.find_elements_by_xpath("")


if __name__ =='__main__':
    ycmlspider("http://gsxt.xjaic.gov.cn:7001/ztxy.do?method=index&flag=fail&djjg=&random=834383618###")