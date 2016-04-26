# -*- coding: utf-8 -*-
#! /usr/bin/env python

from  selenium import  webdriver
import time
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,VARCHAR,create_engine,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from  sqlalchemy.databases import mysql


#数据库配置信息
config = {
    'tablename':'qichacha',
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
class QichachaTable(Base):

    __tablename__=config['tablename']

    url = Column(VARCHAR(255),primary_key=True,index=True,unique=True)
    name = Column(TEXT)
    xym = Column(TEXT)
    jgm = Column(TEXT)
    jyzt = Column(TEXT)
    gstype = Column(TEXT)
    cltime = Column(TEXT)
    fr = Column(TEXT)
    zczb = Column(TEXT)
    yyqx = Column(TEXT)
    djjg = Column(TEXT)
    fztime = Column(TEXT)
    qyaddress = Column(TEXT)
    jyfw = Column(TEXT)
    gdxx = Column(TEXT)
    zyry = Column(TEXT)
    bgjl = Column(TEXT)
    fzjg = Column(TEXT)
    susong = Column(TEXT)
    touzi = Column(TEXT)
    qynb = Column(mysql.LONGTEXT)
    wxzc = Column(TEXT)
    news = Column(TEXT)

    def __init__(self,url,name,xym,jgm,jyzt,gstype,cltime,fr,zczb,yyqx,djjg,fztime,qyaddress,
                 jyfw,gdxx,zyry,bgjl,fzjg,susong,touzi,qynb,wxzc,news):
        self.url = url
        self.name = name
        self.xym = xym
        self.jgm = jgm
        self.jyzt = jyzt
        self.gstype = gstype
        self.cltime = cltime
        self.fr = fr
        self.zczb = zczb
        self.yyqx = yyqx
        self.djjg = djjg
        self.fztime = fztime
        self.qyaddress = qyaddress
        self.jyfw = jyfw
        self.gdxx = gdxx
        self.zyry = zyry
        self.bgjl = bgjl
        self.fzjg = fzjg
        self.susong = susong
        self.touzi = touzi
        self.qynb = qynb
        self.wxzc = wxzc
        self.news = news




    def __repr__(self):
        return "<UserName('%s','%s')>"%(self.name,self.xym)
#创建表
def createAll(engine):
    Base.metadata.create_all(engine)
#删除表
def dropAll(engine):
    Base.metadata.drop_all(engine)

def qichachacookie():

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

    cookies = [{u'name': u'PHPSESSID', u'value': u'2qqrgo3l7422nsngp40ft7hdf4', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'think_language', u'value': u'zh-cn', u'expiry': 1461311621, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'pspt', u'value': u'%7B%22id%22%3A%22250448%22%2C%22pswd%22%3A%228835d2c1351d221b4ab016fbf9e8253f%22%2C%22_code%22%3A%228de0336e04693a20a88a0756a0ff537b%22%7D', u'expiry': 1463900914, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'td_cookie', u'value': u'18446744070600212347', u'expiry': 1463900938, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'SERVERID', u'value': u'b7e4e7feacd29b9704e39cfdfe62aefc|1461308942|1461303588', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'CNZZDATA1254842228', u'value': u'1609020305-1461302633-%7C1461308490', u'expiry': 1477033741, u'path': u'/', u'httpOnly': False, u'secure': False}]
    driver = webdriver.Firefox()
    driver.get("http://qichacha.com/")
    for cookie in cookies:
        driver.add_cookie(cookie)
    urls =[]
    for i in xrange(1,500,1):
        urls.append("http://qichacha.com/gongsi?prov=XJ&p=%s"%i)
    for url in urls:
        driver.get(url)
        for j in xrange(1,len(driver.find_elements_by_xpath("(//a[@class='list-group-item clearfix'])"))+1,1):
            driver.find_element_by_xpath("(//a[@class='list-group-item clearfix'])[%s]"%j).click()
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            time.sleep(5)
            url = driver.current_url
            name = driver.find_element_by_xpath("//div[@class='col-md-8 m-b m-t']//img").get_attribute("alt")
            xym = driver.find_element_by_xpath("//ul[@class='company-base']/li[1]").text
            xym = re.findall(r"\d+",xym)[0]
            jgm = driver.find_element_by_xpath("//ul[@class='company-base']/li[2]").text
            jgm = re.findall(r"\d+",jgm)[0]
            jyzt = driver.find_element_by_xpath("//ul[@class='company-base']/li[3]").text
            jyzt = re.sub(r"经营状态：","",jyzt)
            gstype = driver.find_element_by_xpath("//ul[@class='company-base']/li[4]").text
            gstype = re.sub(r"公司类型：","",gstype)
            cltime = driver.find_element_by_xpath("//ul[@class='company-base']/li[5]").text
            cltime = re.sub(r"成立日期：","",cltime)
            fr = driver.find_element_by_xpath("//ul[@class='company-base']/li[6]").text
            fr = re.sub(r"法定代表：","",fr)
            zczb = driver.find_element_by_xpath("//ul[@class='company-base']/li[7]").text
            zczb = re.sub(r"注册资本：","",zczb)
            yyqx = driver.find_element_by_xpath("//ul[@class='company-base']/li[8]").text
            yyqx = re.sub(r"营业期限：","",yyqx)
            djjg = driver.find_element_by_xpath("//ul[@class='company-base']/li[9]").text
            djjg = re.sub(r"登记机关：","",djjg)
            fztime = driver.find_element_by_xpath("//ul[@class='company-base']/li[10]").text
            fztime = re.sub(r"发照日期：","",fztime)
            qyaddress = driver.find_element_by_xpath("//ul[@class='company-base']/li[11]").text
            qyaddress = re.sub(r"企业地址：","",qyaddress)
            jyfw = driver.find_element_by_xpath("//ul[@class='company-base']/li[12]").text
            jyfw = re.sub(r"经营范围：","",jyfw)
            zdxx = driver.find_elements_by_xpath("//section[@class='panel b-a clear']")
            gdxx=''
            zyry=''
            bgjl=''
            fzjg=''
            for i in zdxx:
                if i.find_element_by_xpath(".//span[@class='font-bold font-15 text-dark']").text ==u'股东信息':
                    gdxx = i.text
                elif i.find_element_by_xpath(".//span[@class='font-bold font-15 text-dark']").text ==u'主要人员':
                    zyry =i.text
                elif i.find_element_by_xpath(".//span[@class='font-bold font-15 text-dark']").text ==u'变更记录':
                    bgjl =i.text
                elif i.find_element_by_xpath(".//span[@class='font-bold font-15 text-dark']").text ==u'分支机构':
                    fzjg =i.text

            driver.find_element_by_xpath("//a[@id='susong_title']").click()
            time.sleep(2)
            susong =driver.find_element_by_xpath("//div[@id='susong_div']").text

            driver.find_element_by_xpath("//a[@id='touzi_title']").click()
            time.sleep(2)
            touzi = driver.find_element_by_xpath("//div[@id='touzi_div']").text

            driver.find_element_by_xpath("//a[@id='report_title']").click()
            time.sleep(2)
            # qynb = driver.find_element_by_xpath("//section[@class='panel pos-rlt  b-a report_info']")
            qynb = driver.page_source

            driver.find_element_by_xpath("//a[@id='assets_title']").click()
            time.sleep(2)
            wxzc = driver.find_element_by_xpath("//div[@id='assets_div']").text

            driver.find_element_by_xpath("//a[@id='job_title']").click()
            time.sleep(2)
            news = driver.find_element_by_xpath("//div[@id='job_div']").text
            print "######################"
            print url
            print name
            # print xym
            # print jgm
            # print jyzt
            # print gstype
            # print cltime
            # print fr
            # print zczb
            # print yyqx
            # print djjg
            # print fztime
            # print qyaddress
            # print jyfw
            # print gdxx
            # print zyry
            # print bgjl
            # print fzjg
            # print susong
            # print touzi
            # print qynb
            # print wxzc
            # print news

            new_user = QichachaTable(url=url,name=name,xym=xym,jgm=jgm,jyzt=jyzt,gstype=gstype,cltime=cltime,
                                fr=fr,zczb=zczb,yyqx=yyqx,djjg=djjg,fztime=fztime,qyaddress=qyaddress,
                                jyfw=jyfw,gdxx=gdxx,zyry=zyry,bgjl=bgjl,fzjg=fzjg,susong=susong,touzi=touzi,
                                qynb=qynb,wxzc=wxzc,news=news
                                     )
            session.add(new_user)

            try:
                session.commit()
            except IntegrityError,e:
                print e.message

            driver.close()
            driver.switch_to_window(windows[0])
    driver.quit()
    session.close()

if __name__ =='__main__':
    qichachacookie()