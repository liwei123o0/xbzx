# -*- coding: utf-8 -*-
#! /usr/bin/env python

from selenium import webdriver
import time
from test.saic import imgorc
from PIL import Image
import MySQLdb

def Fyspider():

    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    while 1:
        cur.execute("SELECT name FROM test.fy_sax WHERE num=0 AND bool=0 LIMIT 1")
        keyword = cur.fetchall()[0][0]
        cur.execute("UPDATE test.fy_sax SET bool=bool+1 WHERE name='%s'"%keyword)
        conn.commit()
        driver.get("http://zhixing.court.gov.cn/search/")
        #识别验证码并进行输入
        png = driver.get_screenshot_as_png()
        with open("yzm.png","wb")as w:
            w.write(png)
        im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm.png")
        box = (468,385,565,430)
        test = im.crop(box)
        test.save("E:\\xbzx\\test\\saic\\spider\\yzm1.png",'png')
        yzm = imgorc.OcrImg('E:\\xbzx\\test\\saic\\spider\\yzm1.png')
        try:
            driver.find_element_by_xpath("//input[@id='pname']").send_keys(keyword)
            driver.find_element_by_xpath("//input[@id='j_captcha']").send_keys(yzm)
            driver.find_element_by_xpath("//button[@id='button']").click()
        except:
            driver.refresh()
        time.sleep(2)

        #验证输入的名字是否合法
        try:
            driver.switch_to_alert().accept()
            cur.execute("UPDATE test.fy_sax SET num=num+999,bool=bool-1 WHERE name='%s'"%keyword)
            conn.commit()
            driver.refresh()
            time.sleep(3)
            continue
        except:
            pass
        try:
            #取iframe的id值做切换
            driver.switch_to.frame('contentFrame')
        except:
            cur.execute("UPDATE test.fy_sax SET bool=bool-1 WHERE name='%s'"%keyword)
            conn.commit()
            continue
        #检查验证码是否有误
        h4 = driver.find_element_by_xpath("//h4").text
        if h4==u"验证码错误，请重新输入！返回首页":
            driver.back()
            driver.switch_to.default_content()
            continue
        else:
            break

    #查询内容循环
    try:
        for i in range(len(driver.find_elements_by_xpath("//a[@class='View']"))):
            driver.find_element_by_xpath("(//a[@class='View'])[%s]"%(i+1 )).click()
            time.sleep(3)
            #内容验证码
            png2 = driver.get_screenshot_as_png()
            with open("yzm2.png","wb")as w:
                w.write(png2)
            im = Image.open("E:\\xbzx\\test\\saic\\spider\\yzm2.png")
            #小屏幕
            box2 = (503,785,584,830)
            #大屏幕
            # box2 = ()
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

        cur.execute("UPDATE test.fy_sax SET num=num+1,bool=bool-1 WHERE name='%s'"%keyword)
        conn.commit()

        cur.close()
        conn.close()
        driver.quit()

    except:
        cur.execute("UPDATE test.fy_sax SET num=num+1,bool=bool-1 WHERE name='%s'"%keyword)
        conn.commit()
        cur.close()
        conn.close()
        driver.quit()

if __name__ =='__main__':

    # Fyspider()
    num = 1

    while 1:

        # try:
        print '############%s#############'%num
        Fyspider()
        # except:
        #     continue
        num+=1