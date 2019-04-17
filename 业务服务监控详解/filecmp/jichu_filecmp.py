#!/usr/bin/python
# -*- coding: utf-8 -*-

import filecmp

#比较单文件差异，相同True，不相同False
print filecmp.cmp("./dir1/f1","./dir2/f2")

#dir1与dir2目录中指定文件清单对比
print filecmp.cmpfiles("./dir1","./dir2",['f1','f2','f3','f4','f5'])
