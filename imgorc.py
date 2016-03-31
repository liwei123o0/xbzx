# -*- coding: utf-8 -*-
#! /usr/bin/env python
import pytesseract
from PIL import  Image
inpath = "E:\\xbzx\\2.png"
#输入图像路径
def OcrImg(inpath):
    image = Image.open(inpath)
    test = pytesseract.image_to_string(image,lang='eng')
    print test

OcrImg(inpath)