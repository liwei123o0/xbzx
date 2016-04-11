# -*- coding: utf-8 -*-
#! /usr/bin/env python
##定义企业注册码校验码计算函数
def getchecknum(input):
    n = 10
    for num in range(len(input)):
        n = (int(input[num]) + n)%10
        if n == 0:
            n = 10
        n = n*2%11
    if n == 0:
        s = 1
    elif n== 1:
        s = 0
    else:
        s = 11-n
    return str(s)

while True:
    code = raw_input(u'请输入该企业15位注册码:')
    try:
        len(code) == 15
        num = code[:14]
        check_num = int(code[14])
        if check_num == int(getchecknum(num)):
            print u'恭喜你，注册码正确。'
            break
        else:
            print u'请注意，该注册码错误！！！'
    except:
        print u"请输入正确的企业15位注册码"