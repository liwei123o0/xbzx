# -*- coding: utf-8 -*-
#! /usr/bin/env python
import urllib2
from lxml import etree
from selenium import webdriver
def getproxy():
    proxes =[]
    driver = webdriver.Firefox()
    driver.get("http://www.xicidaili.com/nn/")
    for i in xrange(len(driver.find_elements_by_xpath("//table[@id='ip_list']//tr[position()>1]/td[3]"))):
        ip = driver.find_element_by_xpath("(//table[@id='ip_list']//tr[position()>1])[%s]/td[3]"%(i+1)).text
        prot = driver.find_element_by_xpath("(//table[@id='ip_list']//tr[position()>1])[%s]/td[4]"%(i+1)).text
        proxy = "%s:%s"%(ip,prot)
        print proxy
        proxes.append(proxy)
    driver.quit()
    return proxes
    # html = urllib2.urlopen("http://www.xicidaili.com/nn/").read()
    # dom = etree.HTML(html)
    # proxes= []
    # for i in xrange(len(dom.xpath("//table[@id='ip_list']//tr[position()>1]/td[3]"))):
    #
    #     ip = dom.xpath("//table[@id='ip_list']//tr[position()>1]/td[3]/text()")
    #     prot = dom.xpath("//table[@id='ip_list']//tr[position()>1]/td[4]/text()")
    #     proxy = "%s:%s"%(ip,prot)
    #     print proxy
    #     proxes.append(proxy)
    # return proxes

def download_page(url, proxy = None, referer = None):
    page_buf = ''
    try:
      # set http proxy
        if proxy:
            handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy})]
            opener =  urllib2.build_opener(*handlers)
        else:
            opener   =  urllib2.build_opener()

        method   =  urllib2.Request(url)
        # set HTTP Referer
        if referer:
            method.add_header('Referer', referer)

        # add user agent
        method.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
        method.add_header('Accept-Language', 'en-US,en;q=0.5')

        result   =  opener.open(method, timeout=10)
        page_buf =  result.read()
    except Exception, reason:
        print 'download failed: ', reason
    return page_buf

def main(proxy):
    url = "https://www.sogou.com/web?query=ip&ie=utf8"
    page_buf = download_page(url,proxy)
    print  page_buf
    dom = etree.HTML(page_buf)
    ipproxy = "".join(dom.xpath("//div[@id='ipsearchresult']/strong/text()"))
    print 'download proxy content: ' + '\n' + ipproxy

if __name__ == '__main__':
    # proxes = getproxy()
    # proxes = ['171.37.117.252:8123','182.88.29.109:8123','182.90.17.107:80','111.176.155.252:3128',
    #           '182.90.8.20:80','113.219.14.38:3128','180.175.73.26:63000','182.90.40.8:80','182.90.18.167:8090',
    #           '182.90.60.203:80','119.138.92.110:8118','14.208.100.252:8118','180.112.219.33:8118']
    proxes =['120.52.73.140:8080','120.52.73.170:80']
    for proxy in proxes:
        main(proxy)