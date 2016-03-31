# -*- coding: utf-8 -*-
#! /usr/bin/env python

import sys
import os
def taskCrawl():
    if len(sys.argv) ==3:
        host = sys.argv[2]
        spidername = sys.argv[1]
        spider = spidername.split("\\")[-1]
        filename = "%s.py"%(spidername)
        if os.path.isfile(filename):
            print u"启动爬虫:\t%s"%spider
        else:
            print u"爬虫文件不存在！"
            return
        os.system("curl http://%s:6800/schedule.json -d project=zbzxtest -d spider=%s"%(host,spider))
    elif len(sys.argv) ==4 and sys.argv[3]=="-add":
        os.system("python scrapyd-deploy.py xbzx -p zbzxtest")
        host = sys.argv[2]
        spidername = sys.argv[1]
        spider = spidername.split("\\")[-1]
        filename = "%s.py"%(spidername)
        if os.path.isfile(filename):
            print u"启动爬虫:\t%s"%spider
        else:
            print u"爬虫文件不存在！"
            return
        os.system("curl http://%s:6800/schedule.json -d project=zbzxtest -d spider=%s"%(host,spider))
    elif len(sys.argv) ==4 and sys.argv[3]=="-d":
        host = sys.argv[2]
        spiderdir = sys.argv[1]
        if os.path.exists(spiderdir):
            spiders = os.listdir(spiderdir)
        else:
            print u"请输入正确的爬虫目录或不存在该目录！"
            return
        for spider in spiders:
            spider = spider.replace(".py","")
            print u"启动爬虫:\t%s"%spider
            os.system("curl http://%s:6800/schedule.json -d project=zbzxtest -d spider=%s"%(host,spider))
    elif len(sys.argv) ==5 and sys.argv[3]=="-d" and sys.argv[4]=="-add":
        os.system("python scrapyd-deploy.py xbzx -p zbzxtest")
        host = sys.argv[2]
        spiderdir = sys.argv[1]
        if os.path.exists(spiderdir):
            spiders = os.listdir(spiderdir)
        else:
            print u"请输入正确的爬虫目录或不存在该目录！"
            return
        for spider in spiders:
            spider = spider.replace(".py","")
            print u"启动爬虫:\t%s"%spider
            os.system("curl http://%s:6800/schedule.json -d project=zbzxtest -d spider=%s"%(host,spider))
    else:
        print u"参数说明：\n" \
              u"\tpath： 第一个参数为爬虫绝对路径或绝对目录路径！\n" \
              u"\thost： 第二个参数为爬虫服务器地址！\n" \
              u"\t以上参数为必填参数！\n" \
              u"注意事项：\n" \
              u"\t-add:  表示新增加爬虫！默认(非新增)\n" \
              u"\t -d    表示为目录路径，默认(爬虫路径)！"
        return

if __name__ =="__main__":
    taskCrawl()