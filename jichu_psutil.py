#!/usr/bin/python
# -*- coding: utf-8 -*-
import psutil,datetime
from subprocess import PIPE

#cpu信息
print "获取cpu完整信息，需要显示所有逻辑cpu信息，指定方法变量percpu=True即可。"
print psutil.cpu_times()
print "获取单项数据，如用户cpu的cpu时间比"
print psutil.cpu_times().user
print "获取cpu的逻辑个数，默认logical=True"
print psutil.cpu_count()
print "获取cpu的物理个数"
print psutil.cpu_count(logical=False)
print

#内存信息
print "获取内存完整信息"
mem = psutil.virtual_memory()
print mem
print "获取内存总数"
print mem.total
print "获取空闲内存数"
print mem.free
print "获取swap分区信息"
print psutil.swap_memory()
print

#磁盘信息
print "获取磁盘完整信息"
print psutil.disk_partitions()
print "获取分区（参数）的使用情况"
print psutil.disk_usage('/')
print "获取硬盘总的IO个数，读写情况"
print psutil.disk_io_counters()
print "perdisk=True参数获取单个分区IO个数，读写情况"
print psutil.disk_io_counters(perdisk=True)
print

#网络信息
print "获取网络总的IO信息，默认pernic=False"
print psutil.net_io_counters()
print "pernic=True输出每个网络接口的IO信息"
print psutil.net_io_counters(pernic=True)
print

#其他系统信息
print "返回当前登录系统的用户信息"
print psutil.users()
print "获取开机时间，以linux时间戳格式返回"
print psutil.boot_time()
print "转换成自然时间格式"
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print

#进程信息
print "列出所有进程PID"
print psutil.pids()
print "实例化一个Process对象，参数为一进程PID"
p = psutil.Process(25672)
print "进程名"
print p.name()
print "进程bin路径"
print p.exe()
#print "进程工作目录绝对路径"
#print p.cwd()
print "进程状态"
print p.status()
print "进程创建时间，时间戳格式"
print p.create_time()
print "进程uid信息"
print p.uids()
print "进程gid信息"
print p.gids()
print "进程cpu时间信息，包括user,system两个cpu时间"
print p.cpu_times()
print "get进程cpu亲和度，如要设置进程cpu亲和度，将cpu号作为参数即可"
print p.cpu_affinity()
print "进程内存利用率"
print p.memory_percent()
print "进程内存rss,vms信息"
print p.memory_info()
#print "进程IO信息，包括读写IO数及字节数"
#print p.io_counters()
#print "返回打开进程socket的namedutples列表，包括fs,family,laddr等信息"
#print p.connections()
print "进程开启的线程数"
print p.num_threads()
print

#popen类的使用
print "通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息"
p = psutil.Popen(["/usr/bin/python","-c","print('hello')"],stdout=PIPE)
print p.name()
print p.username()
print p.communicate()
#print p.cpu_times()