# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import time
from test.saic import imgorc
from PIL import Image

def Fyspider():

    driver = webdriver.Firefox()
    driver.get("http://zhixing.court.gov.cn/search/")

    png = driver.get_screenshot_as_png()

    with open("yzm.png","wb")as w:
        w.write(png)

    im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm.png")

    box = (468,385,565,430)

    test = im.crop(box)

    test.save("E:\\xbzx\\test\\saic\\spider\\yzm1.png",'png')

    yzm = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm1.png')

    driver.find_element_by_xpath("//input[@id='pname']").send_keys(u"陕西")

    driver.find_element_by_xpath("//input[@id='j_captcha']").send_keys(yzm)

    driver.find_element_by_xpath("//button[@id='button']").click()
    time.sleep(2)
    #取iframe的id值做切换
    driver.switch_to.frame('contentFrame')

    driver.find_element_by_xpath("(//a[@class='View'])[1]").click()

    time.sleep(3)

    png2 = driver.get_screenshot_as_png()

    with open("yzm2.png","wb")as w:
        w.write(png2)

    im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm2.png")

    box2 = (503,785,584,830)

    test = im.crop(box2)

    test.save("E:\\xbzx\\test\\saic\\spider\\yzm3.png",'png')

    yzm2 = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm3.png')
    #切换回原窗口
    driver.switch_to.default_content()

    driver.find_element_by_xpath("//input[@id='j_captchad']").send_keys(yzm2)

    driver.find_element_by_xpath("(//div[@class='ui-dialog-buttonset']/button)[1]").click()

    time.sleep(3)

    name = driver.find_element_by_xpath("//td[@id='pnameDetail']").text
    xym = driver.find_element_by_xpath("//td[@id='partyCardNumDetail']").text
    zxfy = driver.find_element_by_xpath("//td[@id='execCourtNameDetail']").text
    latime = driver.find_element_by_xpath("//td[@id='caseCreateTimeDetail']").text
    ah = driver.find_element_by_xpath("//td[@id='caseCodeDetail']").text
    zxb = driver.find_element_by_xpath("//td[@id='execMoneyDetail']").text

    driver.quit()

    print name
    print xym
    print zxfy
    print latime
    print ah
    print zxb

if __name__ =='__main__':
    Fyspider()
    # im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm2.png")
    #
    # box2 = (503,785,584,830)
    #
    # test = im.crop(box2)
    #
    # test.save("E:\\xbzx\\test\\saic\\spider\\yzm3.png",'png')
    #
    # yzm2 = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm3.png')

    # print yzm2

