# -*- coding: utf-8 -*-
#! /usr/bin/env python
from  selenium import webdriver
import urllib2
import time

def load_keyword(path):

    keywords = urllib2.urlopen(path).readlines()
    return keywords

def ccgpspider():

    driver = webdriver.Firefox()
    keywords = load_keyword("http://192.168.10.25/keyword/keyword.txt")
    urls =[]
    for keyword in keywords:
        urls.append("http://search.ccgp.gov.cn/dataB.jsp?searchtype=1&page_index=1&start_time=2016%3A04%3A06&end_time=2016%3A04%3A13&timeType=2&searchchannel=0&dbselect=bidx&kw={}&bidSort=0&pinMu=0&bidType=1&buyerName=&projectId=&displayZone=&zoneId=&agentName=".format(keyword.replace('\r\n','')))
    for url in urls:
        driver.get(url)
        for i in xrange(1,len(driver.find_elements_by_xpath("//ul[@class='vT-srch-result-list-bid']/li"))+1,1):
            try:
                url = driver.find_element_by_xpath("//ul[@class='vT-srch-result-list-bid']/li[%s]/a"%i).get_attribute("href")
                driver.find_element_by_xpath("//ul[@class='vT-srch-result-list-bid']/li[%s]/a"%i).click()
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                title = driver.find_element_by_xpath("//h2").text
                pm = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[3]/td[last()]/p").text
                print url
                print title
                print pm
                driver.close()
                driver.switch_to_window(windows[0])
            except:
                    print "ERROR"
        # try:
        #     driver.find_element_by_xpath("(//a[@class='next'])[1]").click()
        # except:
        #     continue
    driver.quit()
if __name__ =='__main__':
    ccgpspider()