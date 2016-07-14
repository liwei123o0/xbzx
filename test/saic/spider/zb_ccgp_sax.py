# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def ccgp_xy():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver = webdriver.Firefox()
    driver.get('http://www.ccgp-shaanxi.gov.cn/index.jsp')

    driver.find_element_by_xpath("(//td[@id='t2'])[6]").click()
    driver.close()
    windows = driver.window_handles
    driver.switch_to_window(windows[0])

    for j in xrange(1,99,1):
        for  i in  xrange(1,21,1):
            driver.find_element_by_xpath("(//a[@class='b'])[%s]"%i).click()
            time.sleep(0.5)
            win = driver.window_handles
            driver.switch_to_window(win[1])
            try:
                XB_URL = driver.current_url
                XB_TITLE = driver.find_element_by_xpath("//h2").text
                XB_CONTENT = driver.find_element_by_xpath("(//table[@class='td'])[2]").text
                XB_REGION = u"陕西"
                XB_SITENAME = u"陕西招标网-中标公告"
                XB_GROUPNAME = u"招标"
            except:
                driver.close()
                driver.switch_to_window(win[0])
                continue
            # print XB_URL
            print XB_TITLE
            # print XB_CONTENT

            try:
                cur.execute("INSERT INTO spider.zb_ccgp_shaanxi(XB_URL,XB_TITLE,XB_CONTENT,XB_REGION,XB_SITENAME,XB_GROUPNAME)" \
                        " VALUES ('%s','%s','%s','%s','%s','%s')"%(XB_URL,XB_TITLE,XB_CONTENT,XB_REGION,XB_SITENAME,XB_GROUPNAME))
                conn.commit()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

            driver.close()
            driver.switch_to_window(win[0])
        driver.find_element_by_xpath("//form[@name='formBean']//a[last()-1]").click()

    driver.quit()
    cur.close()
    conn.close()
if __name__=='__main__':

    ccgp_xy()