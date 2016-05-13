# -*- coding: utf-8 -*-
#! /usr/bin/env python

'''
    Auth:liwei
    Brief:工商企业异常数据采集(新疆)
    Area:新疆
    Time:2016-5-13
'''

from  selenium import  webdriver
import time
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,VARCHAR,create_engine,TEXT,TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from  sqlalchemy.databases import mysql
#设置入库时间
from sqlalchemy.sql import func

#数据库配置信息
config = {
    'tablename':'gsxx_yc_xj',
    'sql':'mysql',
    'user':'root',
    'password':'root',
    'host':'192.168.10.21',
    'port':'3306',
    'db':'spider',
    'charset':'utf8',
    'echo':True
}

Base = declarative_base()
#建立类与数据库之间映射表
class GsxxTable(Base):

    __tablename__=config['tablename']
    #url去重主键索引设置
    name = Column(VARCHAR(255),primary_key=True,index=True,unique=True)
    xym = Column(TEXT)
    gstype = Column(TEXT)
    fr = Column(TEXT)
    zczb = Column(TEXT)
    cltime = Column(TEXT)
    djzt = Column(TEXT)
    yycs = Column(TEXT)
    yyqx = Column(TEXT)
    yyqxz = Column(TEXT)
    jyfw = Column(TEXT)
    djjg = Column(TEXT)
    hzrq = Column(TEXT)
    #设置入库时间
    insert_time = Column(TIMESTAMP,server_default=func.now())

    def __init__(self,name,xym,gstype,cltime,fr,zczb,djzt,yycs,yyqx,yyqxz,
                 jyfw,djjg,hzrq,insert_time):
        self.name = name
        self.xym = xym
        self.gstype = gstype
        self.cltime = cltime
        self.fr = fr
        self.zczb = zczb
        self.djzt = djzt
        self.yycs = yycs
        self.yyqx = yyqx
        self.yyqxz = yyqxz
        self.djjg = djjg
        self.jyfw = jyfw
        self.hzrq = hzrq
        self.insert_time = insert_time

    def __repr__(self):
        return "<UserName('%s','%s')>"%(self.name,self.xym)
#创建表
def createAll(engine):
    Base.metadata.create_all(engine)
#删除表
def dropAll(engine):
    Base.metadata.drop_all(engine)

def gsqqxx_xj(num):

    #连接数据库
    engine = create_engine('%s://%s:%s@%s:%s/%s?charset=%s'
                       %(config['sql'],config['user'],config['password'],
                         config['host'],config['port'],config['db'],config['charset']),
                       echo=config['echo'])
    #创建会话session
    DBsession = sessionmaker(engine)
    session = DBsession()
    #创建数据库
    createAll(engine)
    # Base.metadata.create_all(engine)
    url =  'http://gsxt.xjaic.gov.cn:7001/xxcx.do?method=ycmlIndex&random=%s&cxyzm=no&entnameold=&djjg=&maent.entname=&page.currentPageNo=%s&yzm='%(int(time.time()),num)

    driver = webdriver.Firefox()
    driver.get(url)

    for k in range(len(driver.find_elements_by_xpath("(//li[@class='tb-a1']/a)"))):
        try:
            driver.find_element_by_xpath("(//li[@class='tb-a1']/a)[%s]"%(k+1)).click()
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            # for i in range(len(driver.find_elements_by_xpath("//div[@id='tabs']//li"))):
            driver.find_element_by_xpath("(//div[@id='tabs']//li)[1]").click()
            time.sleep(0.5)
            djxx =  driver.find_element_by_xpath("(//div[@style='display: block;']//table)[1]").text
            djxx = djxx.encode("utf-8")
            xym = "".join(re.sub("名称.*","","".join(re.findall(r"(?<=统一社会信用代码 ).*",djxx))))
            if xym =="":
                xym = "".join(re.sub("名称.*","","".join(re.findall(r"(?<=注册号 ).*",djxx))))
            name = "".join(re.findall(r"(?<=名称 ).*",djxx))
            gstype = "".join(re.findall(r"(?<=类型 ).*\)",djxx))
            fr = "".join(re.findall(r"(?<=法定代表人 ).*",djxx))
            if fr =="":
                fr = "".join(re.findall(r"(?<=负责人 ).*",djxx))
            if fr =="":
                fr = "".join(re.findall(r"(?<=投资人 ).*",djxx))
            zczb = "".join(re.findall(r"(?<=注册资本 ).*万",djxx))
            cltime = "".join(re.sub("登记状态.*","","".join(re.findall(r"(?<=成立日期).*",djxx))))
            djzt = "".join(re.findall(r"(?<=登记状态 ).*",djxx))
            yycs = "".join(re.findall(r"(?<=营业场所 ).*",djxx))
            if yycs =="":
                yycs = "".join(re.findall(r"(?<=住所 ).*",djxx))
            yyqx = "".join(re.sub("营业期限至.*","","".join(re.findall(r"(?<=营业期限自 ).*",djxx))))
            yyqxz = "".join(re.findall(r"(?<=营业期限至 ).*",djxx))
            jyfw = "".join(re.findall(r"(?<=经营范围).*",djxx))
            djjg = "".join(re.sub("核准日期.*","","".join(re.findall(r"(?<=登记机关 ).*",djxx))))
            hzrq = "".join(re.findall(r"(?<=核准日期 ).*",djxx))

            print jyfw
        except:
            driver.close()
            driver.switch_to_window(windows[0])
            continue
        new_user = GsxxTable(name=name,xym=xym,gstype=gstype,cltime=cltime,
                                    fr=fr,zczb=zczb,djzt=djzt,yycs=yycs,yyqx=yyqx,
                                    yyqxz=yyqxz,jyfw=jyfw,djjg=djjg,hzrq=hzrq,insert_time=func.now())
        session.add(new_user)
        try:
            session.commit()
        except IntegrityError,e:
            print e.message
            session = DBsession()

        driver.close()
        driver.switch_to_window(windows[0])
    driver.quit()
    session.close()

if __name__ =='__main__':

    while 1:
        for i in xrange(1,14526,1):
            try:
                gsqqxx_xj(i)
            except:
                if i ==14526:
                    break
            continue