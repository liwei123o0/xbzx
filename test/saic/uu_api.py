#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

#post方式上传文件及图片
def PostUpData(inpath):
    register_openers()
    api_url = 'http://bbb4.hyslt.com/api.php?mod=php&act=upload'
    data = {'user_name':'877129310@qq.com',
            'user_pw':'1234@asd',
            'yzm_minlen':'',
            'yzm_maxlen':'',
            'yzmtype_mark':'',
            'zztool_token':'',
            'upload':open(inpath,'rb')}
    datagen, headers = multipart_encode(data)
    request = urllib2.Request(api_url,datagen,headers)
    yzm = urllib2.urlopen(request).read()
    word = json.loads(str(yzm))
    word =  word['data']['val']
    return word