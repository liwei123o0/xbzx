# -*- coding: utf-8 -*-
#! /usr/bin/env python

'''
    Auth:liwei
    Brief:企查查数据采集(新疆)
    Area:新疆
    Time:2016-4-28
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
    #url去重主键索引设置
    url = Column(VARCHAR(255),primary_key=True,index=True,unique=True)
    name = Column(TEXT)
    head = Column(TEXT)
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
    #设置入库时间
    insert_time = Column(TIMESTAMP,server_default=func.now())

    def __init__(self,url,name,head,xym,jgm,jyzt,gstype,cltime,fr,zczb,yyqx,djjg,fztime,qyaddress,
                 jyfw,gdxx,zyry,bgjl,fzjg,susong,touzi,qynb,wxzc,news,insert_time):
        self.url = url
        self.name = name
        self.head = head
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
        self.insert_time = insert_time

    def __repr__(self):
        return "<UserName('%s','%s')>"%(self.name,self.xym)
#创建表
def createAll(engine):
    Base.metadata.create_all(engine)
#删除表
def dropAll(engine):
    Base.metadata.drop_all(engine)

def qichachacookie(num):

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
    #有效期半年
    cookies = [{u'name': u'PHPSESSID', u'value': u'2qqrgo3l7422nsngp40ft7hdf4', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'think_language', u'value': u'zh-cn', u'expiry': 1461311621, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'pspt', u'value': u'%7B%22id%22%3A%22250448%22%2C%22pswd%22%3A%228835d2c1351d221b4ab016fbf9e8253f%22%2C%22_code%22%3A%228de0336e04693a20a88a0756a0ff537b%22%7D', u'expiry': 1463900914, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'td_cookie', u'value': u'18446744070600212347', u'expiry': 1463900938, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'SERVERID', u'value': u'b7e4e7feacd29b9704e39cfdfe62aefc|1461308942|1461303588', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'name': u'CNZZDATA1254842228', u'value': u'1609020305-1461302633-%7C1461308490', u'expiry': 1477033741, u'path': u'/', u'httpOnly': False, u'secure': False}]
    driver = webdriver.Firefox()
    driver.get("http://qichacha.com/")
    #添加cookie
    for cookie in cookies:
        driver.add_cookie(cookie)
    urls =[]
    for i in xrange(num,500,1):
        urls.append("http://qichacha.com/gongsi?prov=XJ&p=%s"%i)
    for url in urls:
        driver.get(url)
        for j in xrange(1,len(driver.find_elements_by_xpath("(//a[@class='list-group-item clearfix'])"))+1,1):
            driver.find_element_by_xpath("(//a[@class='list-group-item clearfix'])[%s]"%j).click()
            windows = driver.window_handles
            driver.switch_to_window(windows[1])
            time.sleep(6)
            try:
                url = driver.current_url
                content = driver.find_element_by_xpath("//section[@class='panel b-a base_info']").text
                head = driver.find_element_by_xpath("//small[@class='clear text-ellipsis m-t-xs text-md text-black']").text
                name = driver.find_element_by_xpath("//div[@class='col-md-8 m-b m-t']//img").get_attribute("alt")
                xym = "".join(re.findall(u"(?<=注册号： ).*",content))
                jgm = "".join(re.findall(u"(?<=组织机构代码： ).*",content))
                jyzt = "".join(re.findall(u"(?<=经营状态：).*",content))
                gstype = "".join(re.findall(u"(?<=公司类型：).*",content))
                cltime = "".join(re.findall(u"(?<=成立日期：).*",content))
                fr = "".join(re.findall(u"(?<=法定代表：).*",content))
                zczb = "".join(re.findall(u"(?<=注册资本：).*",content))
                yyqx = "".join(re.findall(u"(?<=营业期限：).*",content))
                djjg = "".join(re.findall(u"(?<=登记机关：).*",content))
                fztime = "".join(re.findall(u"(?<=发照日期：).*",content))
                qyaddress = "".join(re.findall(u"(?<=企业地址：).*",content))
                jyfw = "".join(re.findall(u"(?<=经营范围：).*",content))
                zdxx = driver.find_elements_by_xpath("//section[@class='panel b-a clear']")
            except:
                print driver.current_url
                driver.close()
                driver.switch_to_window(windows[0])
                session = DBsession()
                continue
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
            time.sleep(3)
            susong =driver.find_element_by_xpath("//div[@id='susong_div']").text

            driver.find_element_by_xpath("//a[@id='touzi_title']").click()
            time.sleep(3)
            touzi = driver.find_element_by_xpath("//div[@id='touzi_div']").text

            driver.find_element_by_xpath("//a[@id='report_title']").click()
            time.sleep(3)
            qynb = driver.page_source

            driver.find_element_by_xpath("//a[@id='assets_title']").click()
            time.sleep(3)
            wxzc = driver.find_element_by_xpath("//div[@id='assets_div']").text

            driver.find_element_by_xpath("//a[@id='job_title']").click()
            time.sleep(3)
            news = driver.find_element_by_xpath("//div[@id='job_div']").text
            print "######################"
            print url
            print name

            new_user = QichachaTable(url=url,name=name,head=head,xym=xym,jgm=jgm,jyzt=jyzt,gstype=gstype,cltime=cltime,
                                    fr=fr,zczb=zczb,yyqx=yyqx,djjg=djjg,fztime=fztime,qyaddress=qyaddress,
                                    jyfw=jyfw,gdxx=gdxx,zyry=zyry,bgjl=bgjl,fzjg=fzjg,susong=susong,touzi=touzi,
                                    qynb=qynb,wxzc=wxzc,news=news,insert_time=func.now())
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError,e:
                print e.message
                driver.close()
                driver.switch_to_window(windows[0])

            driver.close()
            driver.switch_to_window(windows[0])
    driver.quit()
    session.close()

if __name__ =='__main__':
    num = 1
    while 1:
        try:
            qichachacookie(num)
        except:
            num+=1
            if num ==500:
                num = 1
            continue