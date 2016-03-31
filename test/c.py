# -*- coding: utf-8 -*-
#! /usr/bin/env python
import MySQLdb
conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
cur  =conn.cursor()
cur.execute("SELECT gszc FROM test.keywords WHERE cout=0 LIMIT 1")
keyword = cur.fetchall()[0][0]
print keyword