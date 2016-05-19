# -*- coding: utf-8 -*-
#! /usr/bin/env python
import urllib2
from lxml import etree

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
    'tablename':'url_gsxx',
    'sql':'mysql',
    'user':'root',
    'password':'root',
    'host':'192.168.10.21',
    'port':'3306',
    'db':'test',
    'charset':'utf8',
    'echo':True
}

Base = declarative_base()
#建立类与数据库之间映射表
class UrlGsxxTable(Base):

    __tablename__=config['tablename']
    #url去重主键索引设置
    url = Column(VARCHAR(255),primary_key=True,index=True,unique=True)
    type_name = Column(VARCHAR(255),index=True,unique=True)
    #设置入库时间
    insert_time = Column(TIMESTAMP,server_default=func.now())

    def __init__(self,url,type_name,insert_time):
        self.url = url
        self.type_name = type_name
        self.insert_time = insert_time

    def __repr__(self):
        return "<UserName('%s','%s')>"%(self.type_name,self.url)
#创建表
def createAll(engine):
    Base.metadata.create_all(engine)
#删除表
def dropAll(engine):
    Base.metadata.drop_all(engine)

def gsxx_urlDB(type_name):


    for num in range(8600,14534,1):
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
        url =  'http://gsxt.xjaic.gov.cn:7001/xxcx.do?method=ycmlIndex&random=%s&cxyzm=no&entnameold=&djjg=&maent.entname=&page.currentPageNo=%s&yzm='%(int(time.time()),num)
        html =  urllib2.urlopen(url).read()
        dom = etree.HTML(html)
        for i in range(len(dom.xpath("//li[@class='tb-a1']/a/@onclick"))):

            id =  "".join(dom.xpath("(//li[@class='tb-a1']/a/@onclick)[%s]"%(i+1)))
            id =  "".join(re.findall("\d+",id))
            gsxx_url = "http://gsxt.xjaic.gov.cn:7001/ztxy.do?method=qyInfo&maent.pripid=%s&czmk=czmk1&from=&random="%id
            print gsxx_url

            new_user = UrlGsxxTable(url=gsxx_url,type_name=type_name,insert_time=func.now())
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError,e:
                print e.message
                session = DBsession()
            session.close()
if __name__ =='__main__':

    gsxx_urlDB("新疆")