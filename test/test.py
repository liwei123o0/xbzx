# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def nameSQL():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    cur.execute("SELECT FRDB FROM test.xypj  LIMIT 1000")
    keyword =cur.fetchall()
    cur.close()
    conn.close()
    return keyword

def crawl():
    keyword = nameSQL()
    driver = webdriver.Firefox()
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    for kk in keyword:
        url = "http://cpquery.sipo.gov.cn/txnQueryOrdinaryPatents.do?&select-key:shenqingrxm=%s"%(kk[0])
        driver.get(url)
        try:
            driver.find_element_by_xpath("//a[@class='content-shenqingh']").click()
            # time.sleep(10)
            url = driver.current_url
            zlh = driver.find_element_by_xpath("(//td[@width='60%']/span)[1]").text
            fmmc = driver.find_element_by_xpath("(//td[@width='60%']/span)[2]").text
            zflh = driver.find_element_by_xpath("(//td[@width='60%']/span)[3]").text
            dljgmc = driver.find_element_by_xpath("(//td[@width='60%']/span)[4]").get_attribute('title')
            dlr = driver.find_element_by_xpath("(//td[@width='60%']/span)[5]").get_attribute('title')
            # try:
            #     cur.execute("INSERT INTO test.sipo(kk,url,zlh,fmmc,zflh,dljgmc,dlr) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(kk[0],url,zlh,fmmc,zflh,dljgmc,dlr))
            # except MySQLdb.Error,e:
            #     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            print kk[0]
            print url
            print zlh
            print fmmc
            print zflh
            print dljgmc
            print dlr
        except:
            continue
    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    crawl()