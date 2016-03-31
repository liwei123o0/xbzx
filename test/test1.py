# -*- coding: utf-8 -*-
#! /usr/bin/env python

from  selenium import webdriver
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import urllib
import urllib2
import mimetypes
import os,stat,sys
import json

api_username = '877129310@qq.com'
api_password = '1234@asd'
api_post_url ='http://bbb4.hyslt.com/api.php?mod=php&act=upload'


class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable

doseq = 1

class MultipartPostHandler(urllib2.BaseHandler):
    handler_order = urllib2.HTTPHandler.handler_order - 10 # needs to run first

    def http_request(self, request):
        data = request.get_data()
        if data is not None and type(data) != str:
            v_files = []
            v_vars = []
            try:
                 for(key, value) in data.items():
                     if type(value) == file:
                         v_files.append((key, value))
                     else:
                         v_vars.append((key, value))
            except TypeError:
                systype, value, traceback = sys.exc_info()
                raise TypeError, "not a valid non-string sequence or mapping object", traceback

            if len(v_files) == 0:
                data = urllib.urlencode(v_vars, doseq)
            else:
                boundary, data = self.multipart_encode(v_vars, v_files)
                contenttype = 'multipart/form-data; boundary=%s' % boundary
                if(request.has_header('Content-Type')
                   and request.get_header('Content-Type').find('multipart/form-data') != 0):
                    print "Replacing %s with %s" % (request.get_header('content-type'), 'multipart/form-data')
                request.add_unredirected_header('Content-Type', contenttype)

            request.add_data(data)
        return request

    def multipart_encode(vars, files, boundary = None, buffer = None):
        if boundary is None:
            boundary = "--1234567890"
        if buffer is None:
            buffer = ''
        for(key, value) in vars:
            buffer += '--%s\r\n' % boundary
            buffer += 'Content-Disposition: form-data; name="%s"' % key
            buffer += '\r\n\r\n' + value + '\r\n'
        for(key, fd) in files:
            file_size = os.fstat(fd.fileno())[stat.ST_SIZE]
            filename = fd.name.split('/')[-1]
            contenttype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            buffer += '--%s\r\n' % boundary
            buffer += 'Content-Disposition: form-data; name="%s"; filename="%s"\r\n' % (key, filename)
            buffer += 'Content-Type: %s\r\n' % contenttype
            fd.seek(0)
            buffer += '\r\n' + fd.read() + '\r\n'
        buffer += '--%s--\r\n\r\n' % boundary
        return boundary, buffer
    multipart_encode = Callable(multipart_encode)
    https_request = http_request

def main(api_username,api_password,img_url,api_post_url,yzm_min='',yzm_max='',yzm_type='',tools_token=''):
    import tempfile

    validatorURL = api_post_url
    opener = urllib2.build_opener(MultipartPostHandler)

    if yzm_min == '' :
        yzm_min = '4'
    if yzm_max == '' :
        yzm_max = '4'

    temp = tempfile.mkstemp(suffix=".png")
    os.write(temp[0],opener.open(img_url).read())
    params = { "user_name"      : '%s' % api_username,
                   "user_pw"        : "%s" % api_password ,
                   "yzm_minlen"     : "%s" % yzm_min ,
                   "yzm_maxlen"     : "%s" % yzm_max ,
                   "yzmtype_mark"   : "%s" % yzm_type ,
                   "zztool_token"   : "%s" % tools_token ,
                   "upload"          : open(temp[1], "rb")
                 }

    value = opener.open(validatorURL, params).read()
    print "value_main:%s"%value
    return value
def FirefoxSpider(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").clear()
    driver.find_element_by_xpath("//div[@class='input-center2']/div[1]/input").send_keys(u"内蒙")
    driver.find_element_by_xpath("//div[@class='input-center2']/div[2]/a").click()

    imgyzm = driver.get_screenshot_as_png()
    with open("temp.png",'wb')as w:
        w.write(imgyzm)
    # imgyzm_url =  driver.find_element_by_xpath("//img[@id='img']").get_attribute("src")

    # yzm = main('877129310@qq.com',
    #      '1234@asd',
    #      imgyzm,
    #      "http://bbb4.hyslt.com/api.php?mod=php&act=upload",
    #      '',
    #      '',
    #      '',)

    # word = json.loads(str(yzm))
    # word =  word['data']['val']
    # print "main:%s"%word
    # driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").clear()
    # driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").send_keys(u"%s"%word)
    # time.sleep(5)
    # driver.find_element_by_xpath("//li[@class='denglu-an']/a").click()
    # while 1:
    #     word=raw_input(u"请输入验证码：")
    #     if word =="":
    #         print u"休眠3秒"
    #         time.sleep(3)
    #         continue
    #     elif word != "":
    #         driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").clear()
    #         driver.find_element_by_xpath("//div[@class='woaicss_con_right']/input").send_keys(u"%s"%word)
    #         driver.find_element_by_xpath("//li[@class='denglu-an']/a").click()
    #         a= driver.switch_to_alert()
    #         try:
    #             a.accept()
    #             continue
    #         except:
    #             break

    time.sleep(5)
    driver.find_element_by_xpath("(//a[@class='font16'])[1] | (//li[@class='font16']/a)[1]").click()
    #获取多个浏览器窗口
    windows = driver.window_handles
    driver.switch_to_window(windows[1])
    title = driver.find_element_by_xpath("//h2").text
    print title
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":

    FirefoxSpider(
        "http://www.nmgs.gov.cn:7001/aiccips/",
    )