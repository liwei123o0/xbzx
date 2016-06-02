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

if __name__ =='__main__':
    # InsertSQL(name='liwei',age=24,sex='男')
    conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    import re
    with open('C:\Users\XBZX\Desktop\ztsj.txt','rb')as f:
        keyword = f.readlines()
    for key in keyword:
        print key
        keys =  re.split('\s+',key)
        try:
            cur.execute("INSERT INTO test.fy_sax(name,xym,fr)" \
                    " VALUES ('%s','%s','%s')"%(keys[1],keys[2],keys[3]))
            conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    cur.close()
    conn.close()