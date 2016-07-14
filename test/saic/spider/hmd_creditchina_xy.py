# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def ccgp_xy():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver = webdriver.Firefox()
    driver.get('http://www.creditchina.gov.cn/search_all#keyword=%E5%92%B8%E9%98%B3&searchtype=0&departmentId=1&creditType=8&page=1')

    for j in xrange(1,5,1):
        for  i in  xrange(1,10,1):
            driver.find_element_by_xpath("(//dl[@class='clearfix'])[%s]/dd[1]/a"%i).click()
            time.sleep(0.5)
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            try:
                XB_URL = driver.current_url
                XB_NAME =driver.find_element_by_xpath("//h1").text
                XB_CONTENT = driver.find_element_by_xpath("//div[@id='dishonestyImg']").text
                XB_REGION = u"陕西-咸阳"
                XB_SITENAME = u"信用中国"
                XB_GROUPNAME = u"失信信息-黑名单"
            except:
                driver.close()
                driver.switch_to_window(windows[0])
                continue
            print XB_URL
            print XB_NAME
            print XB_CONTENT

            try:
                cur.execute("INSERT INTO spider.bcpcn(XB_URL,XB_NAME,XB_CONTENT,XB_REGION,XB_SITENAME,XB_GROUPNAME)" \
                        " VALUES ('%s','%s','%s','%s','%s','%s')"%(XB_URL,XB_NAME,XB_CONTENT,XB_REGION,XB_SITENAME,XB_GROUPNAME))
                conn.commit()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            driver.close()
            driver.switch_to_window(windows[0])
        driver.find_element_by_xpath("//a[@class='page-link next']").click()

    driver.quit()
    cur.close()
    conn.close()
if __name__=='__main__':

    ccgp_xy()