# -*- coding: utf-8 -*-
#! /usr/bin/env python

##按照GB_11714编码规范计算组织机构代码
def zzjgxym(x=''):
    #w为加权码
    w = [3,7,9,10,5,8,4,2]
    num = []
    x = str(x)
    for i in xrange(len(w)):
        n = int(x[i])*w[i]
        num.append(n)
    num = sum(num)
    mod =  divmod(num,11)[1]
    if 11-mod ==10:
        xym ='X'
    elif 11-mod ==11:
        xym=0
    else:
        xym = 11-mod
    return xym
def zzjgm(jgm,xym):
    return "%s%s"%(jgm,xym)


#统一社会信用代码效验码
def tyzzjgxym(x):
    #w为统一社会信用加权码
    w = [1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28]
    num = []
    x = str(x)
    for i in xrange(len(w)):
        if x[i] == 'A':
            n = 10*w[i]
            num.append(n)
        elif x[i] =='B':
            n = 11*w[i]
            num.append(n)
        elif x[i] =='C':
            n = 12*w[i]
            num.append(n)
        elif x[i] =='D':
            n = 13*w[i]
            num.append(n)
        elif x[i] =='E':
            n = 14*w[i]
            num.append(n)
        elif x[i] =='F':
            n = 15*w[i]
            num.append(n)
        elif x[i] =='G':
            n = 16*w[i]
            num.append(n)
        elif x[i] =='H':
            n = 17*w[i]
            num.append(n)
        elif x[i] =='I':
            n = 18*w[i]
            num.append(n)
        elif x[i] =='J':
            n = 19*w[i]
            num.append(n)
        elif x[i] =='K':
            n = 20*w[i]
            num.append(n)
        elif x[i] =='L':
            n = 21*w[i]
            num.append(n)
        elif x[i] =='M':
            n = 22*w[i]
            num.append(n)
        elif x[i] =='N':
            n = 23*w[i]
            num.append(n)
        elif x[i] =='O':
            n = 24*w[i]
            num.append(n)
        elif x[i] =='P':
            n = 25*w[i]
            num.append(n)
        elif x[i] =='Q':
            n = 26*w[i]
            num.append(n)
        elif x[i] =='R':
            n = 27*w[i]
            num.append(n)
        elif x[i] =='S':
            n = 28*w[i]
            num.append(n)
        elif x[i] =='T':
            n = 29*w[i]
            num.append(n)
        elif x[i] =='U':
            n = 30*w[i]
            num.append(n)
        elif x[i] =='V':
            n = 31*w[i]
            num.append(n)
        elif x[i] =='W':
            n = 32*w[i]
            num.append(n)
        elif x[i] =='X':
            n = 33*w[i]
            num.append(n)
        elif x[i] =='Y':
            n = 34*w[i]
            num.append(n)
        elif x[i] =='Z':
            n = 35*w[i]
            num.append(n)
        else:
            n = int(x[i])*w[i]
            num.append(n)
    num = sum(num)
    mod =  divmod(num,31)[1]
    xym = 31-mod
    if xym ==10:
        xym = 'A'
    elif xym ==11:
        xym = 'B'
    elif xym ==12:
        xym = 'C'
    elif xym ==13:
        xym = 'D'
    elif xym ==14:
        xym = 'E'
    elif xym ==15:
        xym = 'F'
    elif xym ==16:
        xym = 'G'
    elif xym ==17:
        xym = 'H'
    elif xym ==18:
        xym = 'J'
    elif xym ==19:
        xym = 'K'
    elif xym ==20:
        xym = 'L'
    elif xym ==21:
        xym = 'M'
    elif xym ==22:
        xym = 'N'
    elif xym ==23:
        xym = 'P'
    elif xym ==24:
        xym = 'Q'
    elif xym ==25:
        xym = 'R'
    elif xym ==26:
        xym = 'T'
    elif xym ==27:
        xym = 'U'
    elif xym ==28:
        xym = 'W'
    elif xym ==29:
        xym = 'X'
    elif xym ==30:
        xym = 'Y'
    elif mod ==0:
        xym = 0
    else:
        xym =  xym
    return xym

def tyzzjgm(jgm,xym):
    return "%s%s"%(jgm,xym)

#验证gb11714
if __name__ =='__main__':
    # first = 9
    # two = [1,2,3,9]
    # qym = 610831
    # for i in two:
    #     num = "%s%s%s"%(first,i,qym)
    #     for j in range(30511100,30511500,1):
    #         zzxym = zzjgxym(j)
    #         jgm = zzjgm(j,zzxym)
    #         num1 = "%s%s"%(num,jgm)
    #         tyxym = tyzzjgxym(num1)
    #         print tyzzjgm(num1,tyxym)
    print tyzzjgxym('91411600783436694')