# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import time
import proxyurllib
#代理方式启动火狐浏览器
def ProxyFirefox(http,prot):
    #启动火狐配置文件
    proxyfile = webdriver.FirefoxProfile()
    #代理设置为开启1表示开启,0表示关闭
    proxyfile.set_preference('network.proxy.type',1)
    #添加代理及端口号
    proxyfile.set_preference('network.proxy.http',http)
    #prot类型为int类型
    proxyfile.set_preference('network.proxy.http_port',prot)
    #添加https的代理及端口号
    proxyfile.set_preference('network.proxy.ssl',http)
    #prot类型为int类型
    proxyfile.set_preference('network.proxy.ssl_port',prot)
    #更新设置
    proxyfile.update_preferences()
    #启动火狐并加载代理设置
    driver = webdriver.Firefox(proxyfile)
    #设置页面请求超时
    driver.set_page_load_timeout(time_to_wait=30)
    try:
        # driver.get("http://gsxt.saic.gov.cn/")
        # driver.get("http://xygs.snaic.gov.cn/ztxy.do?method=index&random=1459844381291")
        # driver.get("https://www.sogou.com/web?query=ip&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&sut=4330&sst0=1459844479628&lkt=0%2C0%2C0")
        driver.get("https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0x81495258000227b3&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=monline_3_dg&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&rsv_sug7=101&rsv_sug2=0&inputT=8&rsv_sug4=1152")
    except :
        print "time out"
        driver.quit()
        return
    print "##########################"
    print http,prot
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    # proxes = proxyurllib.getproxy()
    # for proxy in proxes:
    #     http,prot = proxy.split(":")
    #     ProxyFirefox(http,int(prot))
    ProxyFirefox('124.193.33.233',3128)