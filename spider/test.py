# -*- coding: utf-8 -*-
#! /usr/bin/env python
import chardet
import urllib2
import re
pm = '''
 上海市财政局信息系统等级保护安全测评服务项目的中标公告
中标公告
由上海百通项目管理咨询有限公司组织招标的上海市财政局信息系统等级保护安全测评服务项目（项目编号：SHXM-00-20160316-8479）采购项目，于2016-03-16在上海市政府采购网发布招标信息，2016-04-07 13:30在浦东浦明路1229弄5楼（具体会议室详见电子屏幕）评标。
经评标委员会评审，并经采购人确认，本次评标结果公布如下：
中标信息：

包为“上海市财政局信息系统等级保护安全测评服务项目”的中标供应商：上海市信息安全测评认证中心，中标金额：270000元
中标供应商地址：
 上海市陆家浜路1308号
主要中标标的的名称、规格型号、数量、单价、服务要求或者标的的基本概况：
安全测评范围：门户网站、政府采购、非税收入、预算管理、综合办公、会计管理、外网网络系统和内网网络系统。服务提供商须按照信息系统等级保护测评规范，制定详实的测评方案；在保证测评质量的前提下，按时完成6个信息系统和2套网络系统的等级保护安全测评工作，并于2016年10月30日前提交6个信息系统和2套网络系统的测评报告；根据所测系统的测评报告，提供切实可行的整改技术方案，并协助用户按照技术方案做好所测系统的安全整改工作，直至消除安全隐患。 信息系统测评：40000元；网络系统测评：15000元。
评标委员会成员：
 徐姚晨,秦焕青,曾颖,邬敏华,刘朝旭
如对评标结果有异议，请于本评标结果公布之日起7个工作日内以书面形式向上海百通项目管理咨询有限公司提出质疑。
感谢各供应商单位对本次采购活动的积极参与！
备注：
       采购人： 上海市财政局 采购代理机构： 上海百通项目管理咨询有限公司
地址： 肇嘉浜路800号 地址： 浦东新区浦明路1229弄5楼
邮编： 200030 邮编： 200127
联系人： 刘朝旭 联系人： 周俊
电话： 54679568*16047 电话： 18918322071
传真： 54906010 传真： 50908715
  '''
print re.findall(r"采购人：.*",pm)[0]