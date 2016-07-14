# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

# class ZbzxtestPipeline(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='12312':
#             item['fzdw'] = item['fzdw'].replace(u"发证单位（协会）：","")
#             try:
#                 self.cur.execute("INSERT INTO spider.g12312 ("
#                                  "URL,NAME,XY,ZSBH,FBTIME,YSTIME,FZDW,GSZCH,JHDM,FRDB,ZCZB,SSHY,QYWZ,SSDQ,YB,YYDZ,ZYYW) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['url'],item['name'],item['xy'],item['zsbh'],item['bftime'],item['yxtime'],item['fzdw'],
#                                 item['gszch'],item['jgdm'],item['frdb'],item['zczb'],item['sshy'],item['qywz'],item['ssdq'],
#                                 item['yb'],item['yydz'],item['zyyw'],))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             try:
#                 print u'##################%s###############'%self.cout
#                 # print type(spider.proxy)
#                 # print spider.proxy
#                 print u'url:'+item['url']
#                 print u"公司名称:"+item['name']
#                 print u'信用评级：'+item['xy']
#                 print u'证书编号：'+item['zsbh']
#                 print u'颁发时间：'+item['bftime']
#                 print u'有限时间：'+item['yxtime']
#                 print u'发证单位：'+item['fzdw']
#                 print u'工商注册号：'+item['gszch']
#                 print u'组织机构代码：'+item['jgdm']
#                 print u'法人代表：'+item['frdb']
#                 print u'注册资本：'+item['zczb']
#                 print u'所属行业：'+item['sshy']
#                 print u'企业网址：'+item['qywz']
#                 print u'所属地区：'+item['ssdq']
#                 print u'邮编：'+item['yb']
#                 print u'营业地址：'+item['yydz']
#                 print u'主营业务：'+item['zyyw']
#                 self.cout+=1
#             except:
#                 pass
#         return item
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
# class JrttPipeline(object):
#     def process_item(self, item, spider):
#         if spider.name =='test':
#             print "####################content##########################"
#             print item['content']
#             return item
# class Pipeline12312(object):
#     def open_spider(self,spider):
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='12312search':
#             print "##########12312123123###########"
#             item['bfdw'] = item['bfdw'].replace(u"发证单位（协会）：","")
#             try:
#                 self.cur.execute(u"INSERT INTO test.key12312 ("
#                                  "name,xydj,zsbh,zsrq,yxqz,bfdw,zsdz) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['name'],item['xydj'],item['zsbh'],item['zsrq'],item['yxqz'],item['bfdw'],item['zsdz'],
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             print item['name']
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
# class Pipelinebgcheck(object):
#     def open_spider(self,spider):
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='bgcheck':
#             print "##########bgcheck###########"
#             try:
#                 self.cur.execute(u"INSERT INTO test.bgcheck ("
#                                  "name,xydj,xypm,xyzk,sshy,szdq,gsdz) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['name'],item['xydj'],item['xypm'],item['xyzk'],item['sshy'],item['szdq'],item['gsdz'],
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
# class Pipelineccxi(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='ccxi':
#             print "##########ccxi%s###########"%self.cout
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO spider.ccxi ("
#                                  "url,name,pj,szxpj,spjsj,zzxpj,zpjsj) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['url'],item['name'],item['pj'],item['szxpj'],item['spjsj'],item['zzxpj'],
#                                 item['zpjsj']
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
# class Pipelinepyrating(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='pyrating':
#             print "##########pyrating%s###########"%self.cout
#             print item
#             # for k in item:
#             #     print item
#             #     print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO test.pyrating ("
#                                  "url,name,qytype,ztjb,zjjb,pjzw,pjnd,pjsj) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['url'],item['name'],item['qytype'],item['ztjb'],item['zjjb'],item['pjzw'],item['pjnd'],
#                                 item['pjsj']
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
#
# class Pipelinelhratings(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='lhratings':
#             print "##########lhratings%s###########"%self.cout
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO test.lhratings ("
#                                  "name,ztjb,zw,zxjb,uptime,url) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s')"%(
#                                 item['name'],item['ztjb'],item['zw'],item['zxjb'],item['uptime'],item['url'],
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
# class Pipelinelnqyxypgw(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='lnqyxypgw':
#             print "##########lnqyxypgw%s###########"%self.cout
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             # try:
#             #     self.cur.execute(u"INSERT INTO test.lnqyxypgw ("
#             #                      "name,ztjb,zw,zxjb,uptime,url) VALUES "
#             #                      "('%s','%s','%s','%s','%s','%s')"%(
#             #                     item['name'],item['ztjb'],item['zw'],item['zxjb'],item['uptime'],item['url'],
#             #                     ))
#             #     self.conn.commit()
#             # except MySQLdb.Error,e :
#             #     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
class Pipeline51jobsx(object):
    def open_spider(self,spider):
        self.cout = 0
        # self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
        #本地
        self.conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
        self.cur  =self.conn.cursor()
    def process_item(self, item, spider):
        if spider.name=='51jobsx':
            print "##########51jobsx%s###########"%self.cout
            for k in item:
                print "%s:%s"%(k,item[k])
            try:
                # self.cur.execute(u"INSERT INTO spider.job51sx ("
                self.cur.execute(u"INSERT INTO spider.job51xy ("
                                 "url,name,job,address,pay,pub_date,contact) VALUES "
                                 "('%s','%s','%s','%s','%s','%s','%s')"%(
                                item['url'],item['name'],item['job'],item['address'],item['pay'],item['pub_date'],
                                item['contact']
                                ))
                self.conn.commit()
            except MySQLdb.Error,e :
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            self.cout += 1
    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

# class Pipeline51jobsax(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='51jobsax':
#             print "##########51jobsax%s###########"%self.cout
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO spider.job51sax ("
#                                  "url,name,job,address,pay,pub_date,contact) VALUES "
#                                  "('%s','%s','%s','%s','%s','%s','%s')"%(
#                                 item['url'],item['name'],item['job'],item['address'],item['pay'],item['pub_date'],
#                                 item['contact']
#                                 ))
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
#
# class PipelineBcpcn(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='bcpcn':
#             print "##########bcpcn%s###########"%self.cout
#             print item
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             # try:
#             #     self.cur.execute(u"INSERT INTO spider.bcpcn ("
#             #                      "url,name,cftype,cftime,cfjg) VALUES "
#             #                      "('%s','%s','%s','%s','%s')"%(
#             #                     item['url'],item['name'],item['cftype'],item['cftime'],item['cfjg']
#             #                     ))
#             #     self.conn.commit()
#             # except MySQLdb.Error,e :
#             #     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
#
# class PipelineGsXJ(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='xinjiang':
#             print "##########xinjiang%s###########"%self.cout
#             # print item
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO spider.gsxx_xj_spider("
#                              "url,name,xym,gstype,fr,zczb,cltime,djzt,yycs,yyqx,yyqxz,yywf,djjg,hzrq) VALUES "
#                              "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
#                             item['url'],item['name'],item['xym'],item['gstype'],item['fr'],item['zczb'],item['cltime'],item['djzt'],item['yycs'],item['yyqx'],
#                             item['yyqxz'],item['yywf'],item['djjg'],item['hzrq']
#                             ))
#                 # sql = str(u"INSERT INTO spider.gsxx_xj_spider(name,yywf) VALUES ('%s','%s')"%(item['name'],str(item['yywf'])))
#                 # print sql
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "##############mysql###################"
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()
#
# class PipelineGsSAX(object):
#     def open_spider(self,spider):
#         self.cout = 0
#         self.conn = MySQLdb.connect(host="192.168.10.21",port=3306,user="root",passwd="root",charset="utf8")
#         self.cur  =self.conn.cursor()
#     def process_item(self, item, spider):
#         if spider.name=='shanxi':
#             print "##########shanxi%s###########"%self.cout
#             # print item
#             for k in item:
#                 print "%s:%s"%(k,item[k])
#             try:
#                 self.cur.execute(u"INSERT INTO spider.gsxx_sax_spider("
#                              "url,name,xym,gstype,fr,zczb,cltime,djzt,yycs,yyqx,yyqxz,yywf,djjg,hzrq) VALUES "
#                              "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(
#                             item['url'],item['name'],item['xym'],item['gstype'],item['fr'],item['zczb'],item['cltime'],item['djzt'],item['yycs'],item['yyqx'],
#                             item['yyqxz'],item['yywf'],item['djjg'],item['hzrq']
#                             ))
#                 # sql = str(u"INSERT INTO spider.gsxx_xj_spider(name,yywf) VALUES ('%s','%s')"%(item['name'],str(item['yywf'])))
#                 # print sql
#                 self.conn.commit()
#             except MySQLdb.Error,e :
#                 print "##############mysql###################"
#                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#             self.cout += 1
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()