#!/usr/bin/python
# -*- coding: utf-8 -*-
import psutil

#cpu信息
print "获取cpu完整信息，需要显示所有逻辑cpu信息，指定方法变量percpu=True即可。"
print psutil.cpu_times()
print "获取单项数据，如用户cpu的cpu时间比"
print psutil.cpu_times().user
print "获取cpu的逻辑个数，默认logical=True"
print psutil.cpu_count()
print "获取cpu的物理个数"
print psutil.cpu_count(logical=False)

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

#磁盘信息
print "获取磁盘完整信息"
print psutil.disk_partitions()
print "获取分区（参数）的使用情况"
print psutil.disk_usage('/')
print "获取硬盘总的IO个数，读写情况"
print psutil.disk_io_counters()
print "perdisk=True参数获取单个分区IO个数，读写情况"
print psutil.disk_io_counters(perdisk=True)

