#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import pyclamd
from threading import Thread

class Scan(Thread):
    def __init__(self,IP,scan_type,file):
        """构造方法，参数初始化"""
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""
    def run(self):
        """多进程run方法"""
        try:
            #创建网络套接字连接对象
            cd = pyclamd.ClamdNetworkSocket(self.IP,3310)
            #探测连通性
            if cd.ping():
                self.connstr = self.IP + " connection [OK]"
                #重载clamd病毒特性库，建议更新病毒库后做reload()操作
                cd.reload()
                if self.scan_type == "contscan_file":
                    self.scanresult = "{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n".format(cd.multiscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n".format(cd.scan_file(self.file))
                #线程挂起1秒
                time.sleep(1)
            else:
                self.connstr = self.IP + " ping error,exit"
                return
        except Exception,e:
            self.connstr = self.IP + " " + str(e)

#扫描主机列表
#IPs = ['192.168.1.21','192.168.1.22']
IPs = ['127.0.0.1']
#指扫描模式，支持multiscan_file,contscan_file,scan_file
scantype = "multiscan_file"
#指定扫描路径
scanfile = "/usr/share/nginx/html"
i = 1

#指定启动的线程数
threadnum = 2
#存储扫描Scan类线程对象列表
scanlist = []

for ip in IPs:
    #创建扫描Scan类对象，参数(IP,扫描模式,扫描路径)
    currp = Scan(ip,scantype,scanfile)
    #追加对象到列表
    scanlist.append(currp)

    #当达到指定的线程数或IP列表数后启动，退出线程
    if i%threadnum == 0 or i == len(IPs):
        for task in scanlist:
            #启动线程
            task.start()

        for task in scanlist:
            #等待所有子线程退出，并输出扫描结果
            task.join()
            #打印服务器连接信息
            print task.connstr
            #打印扫描结果
            print task.scanresult
        scanlist = []
    i += 1
