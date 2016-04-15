# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZbzxtestItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    xy  = scrapy.Field()
    zsbh = scrapy.Field()
    bftime = scrapy.Field()
    yxtime = scrapy.Field()
    fzdw    = scrapy.Field()
    gszch    = scrapy.Field()
    jgdm = scrapy.Field()
    frdb  = scrapy.Field()
    zczb   = scrapy.Field()
    sshy    = scrapy.Field()
    qywz    = scrapy.Field()
    ssdq    = scrapy.Field()
    yb    = scrapy.Field()
    yydz      = scrapy.Field()
    zyyw    = scrapy.Field()
    pass

class JrttItem(scrapy.Item):
    content = scrapy.Field()

class Item12312(scrapy.Item):
    name = scrapy.Field()
    xydj = scrapy.Field()
    zsbh = scrapy.Field()
    zsrq = scrapy.Field()
    yxqz = scrapy.Field()
    bfdw = scrapy.Field()
    zsdz = scrapy.Field()

class Itembgcheck(scrapy.Item):
    name = scrapy.Field()
    xydj = scrapy.Field()
    xypm = scrapy.Field()
    xyzk = scrapy.Field()
    sshy = scrapy.Field()
    szdq = scrapy.Field()
    gsdz = scrapy.Field()

class Iitemccxi(scrapy.Item):
    name = scrapy.Field()
    pj = scrapy.Field()
    szxpj = scrapy.Field()
    spjsj = scrapy.Field()
    zzxpj = scrapy.Field()
    zpjsj = scrapy.Field()
    url = scrapy.Field()

class Itempyrating(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    qytype = scrapy.Field()
    ztjb = scrapy.Field()
    zjjb = scrapy.Field()
    pjzw = scrapy.Field()
    pjnd = scrapy.Field()
    pjsj = scrapy.Field()

class Itemlhratings(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    ztjb = scrapy.Field()
    zw = scrapy.Field()
    zxjb = scrapy.Field()
    uptime = scrapy.Field()

class Itemlnqyxypgw(scrapy.Item):
    name = scrapy.Field()
    sxtype = scrapy.Field()
    bsdw = scrapy.Field()
    uptime = scrapy.Field()
    zzjgdm = scrapy.Field()
    fr = scrapy.Field()
    zcd = scrapy.Field()
    hmd = scrapy.Field()
    url = scrapy.Field()

class ItemJob51SX(scrapy.Item):
    url = scrapy.Field()
    job = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    pay = scrapy.Field()
    pub_date = scrapy.Field()
    contact = scrapy.Field()

class ItemJob51SAX(scrapy.Item):
    url = scrapy.Field()
    job = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    pay = scrapy.Field()
    pub_date = scrapy.Field()
    contact = scrapy.Field()

class ItemBcpcn(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    cftype = scrapy.Field()
    cftime = scrapy.Field()
    cfjg = scrapy.Field()
