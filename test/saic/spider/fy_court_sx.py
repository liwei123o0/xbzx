# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import time
from test.saic import imgorc
from PIL import Image
import MySQLdb

def Fyspider():

    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()

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

    driver.find_element_by_xpath("//input[@id='pname']").send_keys(u"宝鸡市")

    driver.find_element_by_xpath("//input[@id='j_captcha']").send_keys(yzm)

    driver.find_element_by_xpath("//button[@id='button']").click()
    time.sleep(2)

    #取iframe的id值做切换
    driver.switch_to.frame('contentFrame')

    #做循环
    for j in range(1,683,1):
        #查询内容循环
        for i in range(len(driver.find_elements_by_xpath("//a[@class='View']"))):

            driver.find_element_by_xpath("(//a[@class='View'])[%s]"%(i+1 )).click()

            time.sleep(3)

            png2 = driver.get_screenshot_as_png()

            with open("yzm2.png","wb")as w:
                w.write(png2)

            im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm2.png")

            box2 = (503,785,584,830)
            # box2 = (503,660,584,695)

            test = im.crop(box2)

            test.save("E:\\xbzx\\test\\saic\\spider\\yzm3.png",'png')

            yzm2 = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm3.png')
            #切换回原窗口
            driver.switch_to.default_content()

            driver.find_element_by_xpath("//input[@id='j_captchad']").send_keys(yzm2)

            driver.find_element_by_xpath("(//div[@class='ui-dialog-buttonset']/button)[1]").click()

            time.sleep(3)

            name = driver.find_element_by_xpath("//td[@id='pnameDetail']").text
            if name == None:
                print "###################"
                continue
            xym = driver.find_element_by_xpath("//td[@id='partyCardNumDetail']").text
            zxfy = driver.find_element_by_xpath("//td[@id='execCourtNameDetail']").text
            latime = driver.find_element_by_xpath("//td[@id='caseCreateTimeDetail']").text
            ah = driver.find_element_by_xpath("//td[@id='caseCodeDetail']").text
            zxb = driver.find_element_by_xpath("//td[@id='execMoneyDetail']").text

            driver.find_element_by_xpath("//button[@id='CloseResultView']").click()

            driver.switch_to.frame('contentFrame')
            print name
            print xym
            print zxfy
            print latime
            print ah
            print zxb
            try:
                cur.execute("INSERT INTO spider.fy_sax_zx(name,xym,zxfy,latime,ah,zxb)" \
                    " VALUES ('%s','%s','%s','%s','%s','%s')"%(name,xym,zxfy,latime,ah,zxb))
                conn.commit()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        while 1:
            #翻页验证码
            print "######翻到第%s页#########"%(j+1)
            driver.find_element_by_xpath("//div[@id='ResultlistBlock']/div/a[last()-1]").click()
            #     driver.find_element_by_xpath("//a[@onclick='gotoPage(%s)']"%(j+1)).click()
            time.sleep(3)

            png2 = driver.get_screenshot_as_png()

            with open("yzm4.png","wb")as w:
                w.write(png2)

            im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm4.png")

            box3 = (503,798,580,821)
            # box3 = (503,663,584,690)

            test = im.crop(box3)

            test.save("E:\\xbzx\\test\\saic\\spider\\yzm5.png",'png')

            yzm3 = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm5.png')

            try:
                yzm3 = int(yzm3)
            except:
                driver.switch_to.default_content()
                driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]").click()
                driver.switch_to.frame('contentFrame')
                continue
            #切换回原窗口
            driver.switch_to.default_content()

            driver.find_element_by_xpath("//input[@id='j_captchad']").send_keys(yzm3)

            driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()

            time.sleep(3)

            driver.switch_to.frame('contentFrame')

            error = driver.find_element_by_xpath("//h4").text

            if error ==u'验证码错误，请重新输入！返回首页':
                driver.back()
                continue
            else:
                break

    cur.close()
    conn.close()
    driver.quit()


if __name__ =='__main__':
    Fyspider()