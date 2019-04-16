#!/usr/bin/python
# -*- coding: utf-8 -*-

from 系统基础信息模块.ipy import IP

#接收用户输入，参数为IP地址或网段地址
ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)
#判断是否为网络地址
if len(ips) > 1:
    print "输出网络地址"
    print('net: %s' % ips.net())
    print "输出网络掩码地址"
    print('netmask: %s' % ips.netmask())
    print "输出网络广播地址"
    print ('broadcast: %s' % ips.broadcast())
    print "输出地址反向解析"
    print ('reverse addreess: %s' % ips.reverseNames()[0])
    print "输出网络子网数"
    print ('subnet: %s' % len(ips))
#为单个IP地址
else:
    print "输出IP反向解析"
    print('reverse address： %s' % ips.reverseNames()[0])
print "输出十六进制地址"
print('hexadecimal: %s' % ips.strHex())
print "输出二进制地址"
print('binary ip: %s' % ips.strBin())
print "输出地址类型"
print('iptype: %s' % ips.iptype())
