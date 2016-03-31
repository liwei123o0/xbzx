# -*- coding: utf-8 -*-
#! /usr/bin/env python
import pytesseract
from PIL import  Image

#输入图像路径
def OcrImg(inpath):
    image = Image.open(inpath)
    test = pytesseract.image_to_string(image,lang='chi_sim')
    print test
    return test
