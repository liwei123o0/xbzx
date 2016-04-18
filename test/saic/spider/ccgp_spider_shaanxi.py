# -*- coding: utf-8 -*-
#! /usr/bin/env python

from  selenium import webdriver
import time
import MySQLdb

def ccpgSpider(num):

    driver = webdriver.Firefox()
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver.get("http://www.ccgp-shaanxi.gov.cn")

    driver.find_element_by_xpath("((//table[@class='bb1'])[2]//td/a)[%s]"%num).click()
    driver.close()
    windos = driver.window_handles
    driver.switch_to_window(windos[1])

    for i in xrange(1,len(driver.find_elements_by_xpath("//a[@class='b']"))+1,1):
        print "#################%s#########################"%i
        driver.find_element_by_xpath("(//a[@class='b'])[%s]"%i).click()
        windos = driver.window_handles
        driver.switch_to_window(windos[2])
        time.sleep(1)

        try:
            url = driver.current_url
            title = driver.find_element_by_xpath("//h2").text
            content = driver.find_element_by_xpath("//td[@class='SaleT01']").text
        except:
            continue

        print url
        print title
        print content

        try:
            cur.execute("INSERT INTO spider.zb_ccgp_shaanxi(url,title,content)" \
              " VALUES ('%s','%s','%s')"%(url,title,content))
            conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        driver.close()
        windos = driver.window_handles
        driver.switch_to_window(windos[1])

    driver.quit()
    cur.close()
    conn.close()

if __name__ =='__main__':

    for i in xrange(1,12,1):
        # try:
            ccpgSpider(i)
        # except:
        #     continue