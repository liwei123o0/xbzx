# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import MySQLdb


driver = webdriver.Firefox()
conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
cur  =conn.cursor()
for i in xrange(1,43,1):
    url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=200300%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9".format(i)
    driver.get(url)
    for i in xrange(len(driver.find_elements_by_xpath("//div[@id='resultList']/div[@class='el']"))):
        XB_URL = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/p//a"%(i+1)).get_attribute('href')
        XB_NAME = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/span[@class='t2']/a"%(i+1)).text
        XB_JOB = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/p//a"%(i+1)).get_attribute('title')
        XB_REGION = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/span[@class='t3']"%(i+1)).text
        XB_PAY = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/span[@class='t4']"%(i+1)).text
        XB_REFRESHTIME = driver.find_element_by_xpath("(//div[@id='resultList']/div[@class='el'])[%s]/span[@class='t5']"%(i+1)).text
        XB_REFRESHTIME = "2016-%s"%XB_REFRESHTIME
        print XB_NAME
        print XB_JOB
        print XB_REGION
        print XB_PAY
        print XB_REFRESHTIME
        try:
            cur.execute("INSERT INTO spider.job51xy(XB_URL,XB_NAME,XB_JOB,XB_REGION,XB_PAY,XB_REFRESHTIME)" \
                        " VALUES ('%s','%s','%s','%s','%s','%s')"%(XB_URL,XB_NAME,XB_JOB,XB_REGION,XB_PAY,XB_REFRESHTIME))
            conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

cur.close()
conn.close()
driver.quit()