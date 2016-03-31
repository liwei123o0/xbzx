# -*- coding: utf-8 -*-
#! /usr/bin/env python
from PIL import Image
#将图片裁剪为验证码尺寸
def jqIMG():
    im = Image.open("E:\\xbzx\\test\\temptest.png")
    box = (350,255,510,320)
    test = im.crop(box)
    test.save('test.png','png')
