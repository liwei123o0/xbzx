# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def crawl():
    driver = webdriver.Firefox()
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    url = "http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html"
    driver.get(url)
    for i in xrange(1,20000,1):
        try:
            for  i in range(len(driver.find_elements_by_xpath("//div[@id='content1']/ul[position()<=last()-1]"))):
                try:
                    uri = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/a[1]"%(i+1)).get_attribute("href")
                    name = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/a[1]"%(i+1)).text
                    xydj = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[1]"%(i+1)).text
                    xypm = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/span[1]"%(i+1)).text
                    xyzk = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/span[2]"%(i+1)).text
                    sshy = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[2]"%(i+1)).text
                    szdq = driver.find_element_by_xpath("//div[@id='content1']/ul[position()<=last()-1][%s]/li/span[1]/a[3]"%(i+1)).text
                except:
                    continue
                try:
                    cur.execute("INSERT INTO spider.bgcheck(url,name,xydj,xypm,xyzk,sshy,szdq) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(
                        uri,name,xydj,xypm,xyzk,sshy,szdq))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                print uri
                print name
                print xydj
                print xypm
                print xyzk
                print sshy
                print szdq
            driver.find_element_by_xpath("//div[@id='AspNetPagerPaging']/a[last()-1]").click()
        except:
            pass
    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    crawl()