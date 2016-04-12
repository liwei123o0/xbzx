# -*- coding: utf-8 -*-
#! /usr/bin/env python

import time
from selenium import webdriver
from test.saic import uu_api,imgtest,proxyfirefox

inpath = 'E:\\xbzx\\test\\saic\\img.png'
outpath = 'E:\\xbzx\\test\\saic\\yzm.png'
proxy = '202.106.16.36'
prot = 3128

#自动实现验证码验证识别登陆
def FirefoxAutoSpider(url):
    #添加代理启动
    proxyfile = proxyfirefox.ProxyFirefox(proxy,prot)
    #打开请求页面
    driver = webdriver.Firefox(proxyfile)
    driver.set_page_load_timeout(time_to_wait=10)
    try:
        driver.get(url)
    except:
        print "time out"
        return
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").clear()
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").send_keys(u"内蒙")
    driver.find_element_by_xpath("//div[@class='input-center2']/div[2]/a").click()
    while 1:
        #获取验证码图片
        imgyzm = driver.get_screenshot_as_png()
        with open(inpath,'wb')as w:
            w.write(imgyzm)
        #将验证码图片截取出来，并保存到指定目录
        imgtest.jqIMG(inpath,outpath)
        #识别验证码，uu大码平台实现
        value = uu_api.PostUpData(outpath)
        #value为unicode值
        print value
        time.sleep(5)
        driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").clear()
        driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").send_keys(value)
        driver.find_element_by_xpath("//li[@class='denglu-an']/a").click()
        time.sleep(3)
        try:
            #验证成功进入搜索页面并选取第一个企业信息
            driver.find_element_by_xpath("(//a[@class='font16'])[1] | (//li[@class='font16']/a)[1]").click()
            # 获取多个浏览器窗口
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            title = driver.find_element_by_xpath("//h2").text
            print title
            break
        except:
            #验证码出错，重新验证
            a = driver.switch_to_alert()
            a.accept()
            print u"验证码有误!"
            continue
    time.sleep(5)
    driver.quit()
#手动输入验证码实现
def FirefoxSpider(url):
    #添加代理启动
    proxyfile = proxyfirefox.ProxyFirefox(proxy,prot)
    #打开请求页面
    driver = webdriver.Firefox(proxyfile)
    #超时设置
    driver.set_page_load_timeout(time_to_wait=10)
    try:
        driver.get(url)
        time.sleep(10)
    except:
        print "time out"
        return
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").clear()
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").send_keys(u"内蒙")
    driver.find_element_by_xpath("//div[@class='input-center2']/div[2]/a").click()
    while 1:
        word=raw_input(u"请输入验证码：").decode("utf8")
        if word =="":
            print u"休眠3秒"
            time.sleep(3)
            continue
        elif word != "":
            driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").clear()
            driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").send_keys(word)
            driver.find_element_by_xpath("//li[@class='denglu-an']/a").click()
            a= driver.switch_to_alert()
            try:
                a.accept()
                print u"验证码有误!"
                continue
            except:
                break
    #验证成功进入搜索页面并选取第一个企业信息
    driver.find_element_by_xpath("(//a[@class='font16'])[1] | (//li[@class='font16']/a)[1]").click()
    # 获取多个浏览器窗口
    windows = driver.window_handles
    driver.switch_to_window(windows[1])
    title = driver.find_element_by_xpath("//h2").text
    print title
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    FirefoxSpider(
        "http://www.nmgs.gov.cn:7001/aiccips/"
    )
    # FirefoxAutoSpider(
    #     "http://www.nmgs.gov.cn:7001/aiccips/",
    # )