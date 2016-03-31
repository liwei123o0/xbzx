# -*- coding: utf-8 -*-
#! /usr/bin/env python
from PIL import Image
#将图片裁剪为验证码尺寸
def jqIMG(path,outpath):
    im = Image.open(path)
    box = (350,255,510,320)
    test = im.crop(box)
    test.save(outpath,'png')
