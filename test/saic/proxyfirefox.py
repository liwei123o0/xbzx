# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import time
#代理方式启动火狐浏览器
def ProxyFirefox():
    #启动火狐配置文件
    proxyfile = webdriver.FirefoxProfile()
    #代理设置为开启1表示开启,0表示关闭
    proxyfile.set_preference('network.proxy.type',1)
    #添加代理及端口号
    proxyfile.set_preference('network.proxy.http','202.106.16.36')
    #prot类型为int类型
    proxyfile.set_preference('network.proxy.http_port',3128)
    #添加https的代理及端口号
    proxyfile.set_preference('network.proxy.ssl','202.106.16.36')
    #prot类型为int类型
    proxyfile.set_preference('network.proxy.ssl_port',3128)
    #更新设置
    proxyfile.update_preferences()
    #启动火狐并加载代理设置
    driver = webdriver.Firefox(proxyfile)
    #设置页面请求超时
    driver.set_page_load_timeout(time_to_wait=10)
    try:
        driver.get("http://gsxt.saic.gov.cn/")
        driver.get("https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0x81495258000227b3&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=monline_3_dg&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&rsv_sug7=101&rsv_sug2=0&inputT=8&rsv_sug4=1152")
    except :
        print "time out"
    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    ProxyFirefox()