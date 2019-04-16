#!/usr/bin/python
# -*- coding: utf-8 -*-

import dns.resolver

#输入域名地址
domain = raw_input('Please input an domain: ')

#指定查询类型为A记录
A = dns.resolver.query(domain,'A')

#通过response.answer方法获取查询回应信息
for i in A.response.answer:
    #遍历回应信息
    for j in i.items:
        print j.address