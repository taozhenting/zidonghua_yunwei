#!/usr/bin/python
# -*- coding: utf-8 -*-

from IPy import IP

ip = IP('192.168.0.0/31')
print "输出192.168.0.0/31网段的IP个数"
print ip.len()
print "输出192.168.0.0/31网段的所有IP清单"
for x in ip:
    print(x)

ip = IP('192.168.0.1')
print "反向解析地址格式"
print ip.reverseNames()
print "网络类型"
print ip.iptype()
print IP('8.8.8.8').iptype()
print "转换成整型格式"
print ip.int()
print "转换成十六进制格式"
print ip.strHex()
print "转换成二进制格式"
print ip.strBin()
print "十六进制转成IP格式"
print(IP(0xc0a80001))
print "网络地址转换"
print (IP('192.168.0.0').make_net('255.255.255.0'))
print (IP('192.168.0.0/255.255.255.0',make_net=True))
print (IP('192.168.0.0-192.168.0.255',make_net=True))
print "通过strNormal方法指定不同参数定制不同输出类型的网段"
print IP('192.168.0.0/24').strNormal(0)
print IP('192.168.0.0/24').strNormal(1)
print IP('192.168.0.0/24').strNormal(2)
print IP('192.168.0.0/24').strNormal(3)
print "判断IP地址和网段是否包含于另一个网段中"
print '192.168.0.100' in IP('192.168.0.0/24')
print IP('192.168.0.0/24') in IP('192.168.0.0/16')
print "判断两个网段是否存在重叠,返回1代表重叠，返回0代码不重叠"
print IP('192.168.0.0/23').overlaps('192.168.0.0/24')
print IP('192.168.0.0/24').overlaps('192.168.1.0')