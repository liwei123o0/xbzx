# -*- coding: utf-8 -*-
#! /usr/bin/env python
from  selenium import webdriver
import urllib2
import MySQLdb

def load_keyword(path):

    keywords = urllib2.urlopen(path).readlines()
    return keywords

def ccgpspider():
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver = webdriver.Firefox()
    keywords = load_keyword("http://192.168.10.25/keyword/keyword.txt")
    urls =[]
    for keyword in keywords:
        urls.append("http://search.ccgp.gov.cn/dataB.jsp?searchtype=1&page_index=1&start_time=2016%3A04%3A06&end_time=2016%3A04%3A13&timeType=7&searchchannel=0&dbselect=bidx&kw={}&bidSort=0&pinMu=0&bidType=7&buyerName=&projectId=&displayZone=&zoneId=&agentName=".format(keyword.replace('\r\n','')))
    for url in urls:
        driver.get(url)
        for i in xrange(1,len(driver.find_elements_by_xpath("//ul[@class='vT-srch-result-list-bid']/li"))+1,1):
            try:
                driver.find_element_by_xpath("//ul[@class='vT-srch-result-list-bid']/li[%s]/a"%i).click()
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                try:
                    driver.find_element_by_xpath("//span[@id='displayGG']").click()
                except:
                    pass
                url = driver.current_url
                title = driver.find_element_by_xpath("//h2").text
                content = driver.find_element_by_xpath("//div[@class='vT_detail_content w760c']").text
                zbtype = u"中标公告"
                try:
                    cur.execute("INSERT INTO spider.zb_ccgp_zbgg(url,title,content,zbtype) VALUES ("
                                "'%s','%s','%s','%s')"%(url,title,content,zbtype))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

                print url
                print title
                print content
                print zbtype

                driver.close()
                driver.switch_to_window(windows[0])
            except:
                driver.close()
                driver.switch_to_window(windows[0])
                print "ERROR"
                continue

    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    ccgpspider()