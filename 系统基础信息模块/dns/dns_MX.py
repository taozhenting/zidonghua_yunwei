#!/usr/bin/python
# -*- coding: utf-8 -*-

import dns.resolver

#输入域名地址
domain = raw_input('Please input an domain: ')

#指定查询类型为MX记录
MX = dns.resolver.query(domain,'MX')

#遍历回应结果，输出MX记录的preference及exchanger信息
for i in MX:
    print 'MX preference =',i.preference,'mail exchanger=',i.exchange