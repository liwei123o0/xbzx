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
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    urls = ['http://search.51job.com/list/200200%252C00,%2B,%2B,%2B,%2B,%2B,%25CE%25F7%25B0%25B2,1,%2B.html?lang=c&stype=1&image_x=34&image_y=11&specialarea=00',
                  'http://search.51job.com/list/200200%252C00,000000,0000,00,9,99,%25CE%25F7%25B0%25B2,2,2.html?lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=9&dibiaoid=0',
                  'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=200200%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E8%A5%BF%E5%AE%89&keywordtype=2&curr_page=3&lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9',
                  'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=200200%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E8%A5%BF%E5%AE%89&keywordtype=2&curr_page=4&lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9']

    for url in urls:
        driver.get(url)
        time.sleep(5)
        try:
            for i in range(len(driver.find_elements_by_xpath("//div[@class='dw_table']//div[@class='el']"))):
                zwname = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/p//a"%(i+1)).get_attribute("title")
                name = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/span[@class='t2']/a"%(i+1)).get_attribute("title")
                dd  = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/span[@class='t3']"%(i+1)).text
                xz  = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/span[@class='t4']"%(i+1)).text
                pub_time  = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/span[@class='t5']"%(i+1)).text
                pub_time = u"2016-%s"%pub_time
                url = driver.find_element_by_xpath("//div[@class='dw_table']//div[@class='el'][%s]/p/a"%(i+1)).get_attribute("href")
                print url
                print name
                print zwname
                print dd
                print xz
                print pub_time
                try:
                    cur.execute("INSERT INTO test.job51(name,zwname,dd,xz,pub_time,url) VALUES ('%s','%s','%s','%s','%s','%s')"%(
                        name,zwname,dd,xz,pub_time,url))
                    conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        except:
            cur.close()
            conn.close()
            driver.quit()
            pass
    cur.close()
    conn.close()
    driver.quit()
if __name__ =='__main__':
    crawl()