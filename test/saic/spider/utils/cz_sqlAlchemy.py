# -*- coding: utf-8 -*-
#! /usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,VARCHAR,create_engine,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

#数据库配置信息
config = {
    'tablename':'users',
    'sql':'mysql',
    'user':'root',
    'password':'root',
    'host':'localhost',
    'port':'3306',
    'db':'test',
    'charset':'utf8',
    'echo':True
}

Base = declarative_base()
#建立类与数据库之间映射表
class UserName(Base):

    __tablename__=config['tablename']

    url = Column(VARCHAR(255),primary_key=True,index=True,unique=True)
    name = Column(TEXT)
    content = Column(VARCHAR(255))

    def __init__(self,url,name,content):
        self.url = url
        self.name = name
        self.content = content

    def __repr__(self):
        return "<UserName('%s','%s')>"%(self.name,self.content)
#创建表
def createAll(engine):
    Base.metadata.create_all(engine)
#删除表
def dropAll(engine):
    Base.metadata.drop_all(engine)

if __name__ =='__main__':
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

    new_user = UserName(url="http://www.baidu.com",name='liwei',content='李伟')
    session.add(new_user)
    try:
        session.commit()
    except IntegrityError,e:
        print e.message
    session.close()