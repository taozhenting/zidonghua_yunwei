#!/usr/bin/python
# -*- coding: utf-8 -*-

import dns.resolver
import os
import httplib

#定义域名IP列表变量
iplist = []
#定义业务域名
appdomain = "www.ichile.com.cn"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

print get_iplist(appdomain)

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    #定义http链接超时时间5秒
    httplib.socket.setdefaulttimeout(5)
    #创建http链接对象
    conn = httplib.HTTPConnection(checkurl)

    try:
        #发起URL请求，添加host主机头
        conn.request("GET", "/",headers = {"Host": appdomain})
        r = conn.getresponse()
        #获取URL页面前15个字符，以便做可用性校验
        getcontent = r.read(15)

    #不管是否发生异常，finally都会执行
    finally:
        #监控URL页的内容一般是事先定义好的，比如"HTTP200"等
        #print getcontent
        #if getcontent == "<!doctype html>":
        print r.status
        if r.status == 200:
            print ip+" [OK]"
        else:
            #此处可放告警程序，可以是邮件，短信通知
            print ip+" [Error]"

"""
通俗的理解__name__ == '__main__'：假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')。
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
"""
if __name__ == "__main__":
    #条件：域名解析正确且至少返回一个IP
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."

