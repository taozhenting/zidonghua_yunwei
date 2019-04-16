#!/usr/bin/python
# -*- coding: utf-8 -*-

import dns.resolver

#输入域名地址
domain = raw_input('Please input an domain: ')

#指定查询类型为CNAME记录
cname = dns.resolver.query(domain,'CNAME')

#结果将回应cname后的目标域名
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()