# -*- coding: utf-8 -*-
#! /usr/bin/env python
from  selenium import webdriver
import urllib2
import MySQLdb

def load_keyword(path):

    keywords = urllib2.urlopen(path).readlines()[0]
    keywords = keywords.split('\r')
    return keywords

def ccgpspider():
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    driver = webdriver.Firefox()
    keywords = load_keyword("http://127.0.0.1/keywords/keyword.txt")
    urls =[]
    for keyword in keywords:
        urls.append("http://search.ccgp.gov.cn/dataB.jsp?searchtype=1&page_index=1&start_time=2016%3A04%3A06&end_time=2016%3A04%3A13&timeType=2&searchchannel=0&dbselect=bidx&kw={}&bidSort=0&pinMu=0&bidType=1&buyerName=&projectId=&displayZone=&zoneId=&agentName=".format(keyword.replace('\r\n','')))
    for url in urls[159:]:
        driver.get(url)

        for i in xrange(1,len(driver.find_elements_by_xpath("//ul[@class='vT-srch-result-list-bid']/li"))+1,1):
            try:
                driver.find_element_by_xpath("//ul[@class='vT-srch-result-list-bid']/li[%s]/a"%i).click()
                windows = driver.window_handles
                driver.switch_to_window(windows[1])
                url = driver.current_url
                title = driver.find_element_by_xpath("//h2").text
                pm = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[3]/td[last()]/p").text
                cgr = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[4]/td[last()]").text
                xzqy = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[5]/td[last()-2]").text
                ggsj = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[5]/td[last()]").text
                filetime = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[6]/td[last()]").text
                fileprice = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[7]/td[last()]").text
                fileaddress = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[8]/td[last()]").text
                kbtime = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[9]/td[last()]").text
                kbaddress = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[10]/td[last()]").text
                budget = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[11]/td[last()]").text
                xmlxr = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[13]/td[last()]").text
                xmlxdh = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[14]/td[last()]").text
                cgrdz = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[16]/td[last()]").text
                cgrdh = driver.find_element_by_xpath("//div[@class='table']//tbody/tr[17]/td[last()]").text
                zbtype = u"公开招标"

                try:
                    cur.execute("INSERT INTO spider.zb_ccgp_gkzb("
                                "url,title,pm,cgr,xzqy,ggsj,filetime,fileprice,fileaddress,kbtime,"
                                "kbaddress,budget,xmlxr,xmlxdh,cgrdz,cgrdh,zbtype) VALUES ("
                                "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"
                                "'%s','%s','%s','%s','%s')"%(
                        url,title,pm,cgr,xzqy,ggsj,filetime,fileprice,fileaddress,kbtime,
                        kbaddress,budget,xmlxr,xmlxdh,cgrdz,cgrdh,zbtype))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

                print url
                print title
                print pm
                print cgr
                print xzqy
                print ggsj
                print filetime
                print fileprice
                print fileaddress
                print kbtime
                print kbaddress
                print budget
                print xmlxr
                print xmlxdh
                print cgrdz
                print cgrdh
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