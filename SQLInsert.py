# -*- coding: utf-8 -*-
#! /usr/bin/env python
import MySQLdb

def InsertSQL(*args,**kwargs):
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  = conn.cursor()
    cur.execute("INSERT INTO spider.proxes (args) VALUES ('%s','%s')"%(kwargs[args],kwargs[args]))
    conn.commit()

    for key in kwargs:
        print "%s:%s"%(key,kwargs[key])
    pass

if __name__ =='__main__':
    InsertSQL(name='liwei',age=24,sex='男')
