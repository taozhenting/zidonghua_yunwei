#!/usr/bin/python
# -*- coding: utf-8 -*-

import filecmp

#定义左目录
a = "./dir1"
#定义右目录
b = "./dir2"
#目录比较，忽略test.py文件
dirobj = filecmp.dircmp(a,b,['test.py'])

#输出对比结果数据报表
#比较当前指定目录中的内容
dirobj.report()
#比较当前指定目录及第一级子目录中的内容
dirobj.report_partial_closure()
#递归比较所有指定目录的内容
dirobj.report_full_closure()

print "左目录中的文件及目录列表:" + str(dirobj.left_list)
print "右目录中的文件及目录列表:" + str(dirobj.right_list)
print "两边目录共同存在的文件或目录:" + str(dirobj.common)
print "只在左目录中的文件或目录:" + str(dirobj.left_only)
print "只在右目录中的文件或目录:" + str(dirobj.right_only)
print "两边目录都存在的子目录:" + str(dirobj.common_dirs)
print "两边目录都存在的子文件" + str(dirobj.common_files)
print "两边目录都存在的子目录(不同目录型或os.stat()记录的错误):" + str(dirobj.common_funny)
print "匹配相同的文件:" + str(dirobj.same_files)
print "不匹配的文件:" + str(dirobj.diff_files)
print "两边目录中都存在，但无法比较的文件:" + str(dirobj.funny_files)