#!/usr/bin/python
# -*- coding: utf-8 -*-

import pycurl

#创建一个curl对象
c = pycurl.Curl()

#setopt方法
#连接的等待时间，设置为0则不等待
c.setopt(pycurl.CONNECTTIMEOUT, 5)
#请求超时时间
c.setopt(pycurl.TIMEOUT, 5)
#是否屏蔽下载进度条，非0则屏蔽
c.setopt(pycurl.NOPROGRESS, 0)
#指定HTTP重定向的最大数
c.setopt(pycurl.MAXREDIRS, 5)
#完成交互后强制断开连接，不重用
c.setopt(pycurl.FORBID_REUSE, 1)
#强制获取新的连接，即替代缓存中的连接
c.setopt(pycurl.FRESH_CONNECT, 1)
#设置保存DNS信息的时间，默认为120秒
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)
#指定请求的URL
c.setopt(pycurl.URL, "http://www.gw.com.cn")
#配置请求HTTP头的User-Agent
c.setopt(pycurl.USERAGENT,"Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")
#将返回的HTTP HEADER定向到回调函数getheader
#c.setopt(pycurl.HEADERFUNCTION, getheader)
#将返回的内容定向到回调函数getbody
#c.setopt(pycurl.WRITEFUNCTION, getbody)
#将返回HTTP HEADER定向到fileobj文件对象
#c.setopt(pycurl.WRITEHEADER, fileobj)
#将返回的HTML内容定向到fileobj文件对象
#c.setopt(pycurl.WRITEDATA, fileobj)

#getinfo方法
#返回的HTTP状态码
c.getinfo(pycurl.HTTP_CODE)
#传输结束所消耗的总时间
c.getinfo(pycurl.TOTAL_TIME)
#DNS解析所消耗的时间
c.getinfo(pycurl.NAMELOOKUP_TIME)
#建立连接所消耗的时间
c.getinfo(pycurl.CONNECT_TIME)
#从建立连接到准备传输所消耗的时间
c.getinfo(pycurl.PRETRANSFER_TIME)
#从建立连接到传输开始消耗的时间
c.getinfo(pycurl.STARTTRANSFER_TIME)
#重定向所消耗的时间
c.getinfo(pycurl.REDIRECT_TIME)
#上传数据包大小
c.getinfo(pycurl.SIZE_UPLOAD)
#下载数据包大小
c.getinfo(pycurl.SIZE_DOWNLOAD)
#平均下载速度
c.getinfo(pycurl.SPEED_DOWNLOAD)
#平均上传速度
c.getinfo(pycurl.SPEED_UPLOAD)
#HTTP头部大小
c.getinfo(pycurl.HEADER_SIZE)