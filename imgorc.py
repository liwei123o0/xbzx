# -*- coding: utf-8 -*-
#! /usr/bin/env python
import pytesseract
from PIL import  Image
# inpath = "E:\\xbzx\\2.png"
#输入图像路径
def OcrImg(inpath):
    image = Image.open(inpath)
    test = pytesseract.image_to_string(image,lang='eng')
    print test

if __name__ =='__main__':
    import MySQLdb
    # import os
    # inpaths = os.listdir("E:\\xbzx\\yzm")
    # for inpath in inpaths:
    #     inpath = "E:\\xbzx\\yzm\\%s"%inpath
    #
    #     print "%s:\n"%inpath
    #     OcrImg(inpath)
    # OcrImg("E:\\xbzx\\1.png")
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    cur.execute("SELECT url FROM test.url_gsxx")
    urls = cur.fetchall()
    for i in urls:
        print type(str(i[0]))
    cur.close()
    conn.close()
