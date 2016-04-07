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
    driver = webdriver.Firefox()
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    url = "http://rcpu.cwun.org/Judge.aspx"
    driver.get(url)
    for i in xrange(1,37,1):
        try:
            url = driver.current_url
            for  i in range(len(driver.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()>1]"))-1):
                name = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[2]"%(i+2)).text
                sqtype = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[3]"%(i+2)).text
                xydj = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[4]"%(i+2)).text
                pjnd = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[5]"%(i+2)).text
                bfrq = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[6]"%(i+2)).text
                yxqz = driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_GridViewJudge']//tr[position()=%s]/td[7]"%(i+2)).text
                try:
                    cur.execute("INSERT INTO spider.rcpu(url,name,sqtype,xydj,pjnd,bfrq,yxqz) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(
                        url,name,sqtype,xydj,pjnd,bfrq,yxqz))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                print url
                print name
                print sqtype
                print xydj
                print pjnd
                print bfrq
                print yxqz

            driver.find_element_by_xpath("//a[@id='ContentPlaceHolder1_GridViewJudge_LinkButtonNextPage']").click()
            time.sleep(3)
        except:
        #     cur.close()
        #     conn.close()
        #     driver.quit()
            pass
    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    crawl()