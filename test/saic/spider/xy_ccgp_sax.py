# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def ccgp_xy():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver = webdriver.Firefox()
    driver.get('http://www.bgcheck.cn/MemberCenter/FirmCredit/Search.html?Keywords=%25E5%2592%25B8%25E9%2598%25B3')

    for j in xrange(1,30,1):
        for  i in  xrange(1,11,1):
            try:
                XB_URL = driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/a)[%s]"%i).get_attribute("href")
                XB_NAME =driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/a[last()-1])[%s]"%i).text
                XB_XYDJ = driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/span/a[1])[%s]"%i).text
                XB_XYPM = driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/span/span[1])[%s]"%i).text
                XB_XYZK = driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/span/span[2])[%s]"%i).text
                XB_SHHY = driver.find_element_by_xpath("(//div[@id='content1']/ul//li[1]/span//a[2])[%s]"%i).text
                XB_REGION = u"陕西-咸阳"
                XB_SITENAME = u"企业信用网"
                XB_GROUPNAME = u"评估"
            except:
                continue
            print XB_URL
            print XB_NAME
            print XB_XYDJ
            print XB_XYPM
            print XB_XYZK
            print XB_SHHY

            try:
                cur.execute("INSERT INTO spider.xy_bgcheck_xy(XB_URL,XB_NAME,XB_XYDJ,XB_XYPM,XB_XYZK,XB_SHHY,XB_REGION,XB_SITENAME,XB_GROUPNAME)" \
                        " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(XB_URL,XB_NAME,XB_XYDJ,XB_XYPM,XB_XYZK,XB_SHHY,XB_REGION,XB_SITENAME,XB_GROUPNAME))
                conn.commit()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

        driver.find_element_by_xpath("//div[@id='AspNetPagerPaging']/a[last()-1]").click()

    driver.quit()
    cur.close()
    conn.close()
if __name__=='__main__':

    ccgp_xy()