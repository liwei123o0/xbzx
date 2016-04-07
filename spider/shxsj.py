# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb
import time

def crawl():
    driver = webdriver.Firefox()
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    urls = []
    for i in xrange(1,260,1):
        urls.append("http://www.shxsj.com/lists.php?page=%s&menuid=107&catid=82"%i)
    for url in urls:
        driver.get(url)
        try:
            for  i in range(1,len(driver.find_elements_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])/td[2]/a"))*2,1):
                try:
                    uri = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[2]/a"%i).get_attribute("href")
                    name = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[2]/a"%i).text
                    pjtype = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[3]"%(i)).text
                    ztpj = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[4]"%(i)).text
                    pjzw = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[5]"%(i)).text
                    zxpj = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[6]"%(i)).text
                    pjtime = driver.find_element_by_xpath("((//table/tbody/tr[5])[2]//tr[position()<=last()-1 and position()>1])[%s]/td[7]"%(i)).text
                except:
                    continue
                try:
                    cur.execute("INSERT INTO spider.shxsj(url,name,pjtype,ztpj,pjzw,zxpj,pjtime) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(
                        uri,name,pjtype,ztpj,pjzw,zxpj,pjtime))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                print uri
                print name
                print pjtype
                print ztpj
                print pjzw
                print zxpj
                print pjtime
        except:
            pass
    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    crawl()