# -*- coding: utf-8 -*-
#! /usr/bin/env python
import json
import MySQLdb
def content():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    with open('content.txt','rb')as f:
        words = f.readlines()

    for w in words:

        s= json.loads(w)
        name = s['pname']
        ah = s['caseCode']
        zxfy = s['execCourtName']
        xym = s['partyCardNum']
        zxb = s['execMoney']
        latime = s['caseCreateTime']

        print "name:"+name
        print "ah:"+ah
        print "zxfy:"+zxfy
        print "xym:"+xym
        print "zxb:%s"%zxb
        print "latime"+latime

        try:
            cur.execute("INSERT INTO spider.fy_sax_zx(name,xym,zxfy,latime,ah,zxb)" \
                    " VALUES ('%s','%s','%s','%s','%s','%s')"%(name,xym,zxfy,latime,ah,zxb))
            conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    cur.close()
    conn.close()

if __name__ =='__main__':

    import urllib2
    url='http://www.ccgp-shaanxi.gov.cn/zbAll_view.jsp?ClassName=C0002&pages=1'

    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip',
    'Connection':'close',
    'Referer':'	http://www.ccgp-shaanxi.gov.cn/top.jsp' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
    }
    req_timeout = 5
    req = urllib2.Request(url,None,req_header)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = resp.read()

    print html.decode("gbk")
