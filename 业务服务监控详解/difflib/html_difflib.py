#!/usr/bin/python
# -*- coding: utf-8 -*-

import difflib
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

#以行进行分隔，以便进行对比
text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
"""

text2_lines = text2.splitlines()

#使用HtmlDiff类的make_file方法就可以生成美观的html文档
d = difflib.HtmlDiff()
#生成的html文件名
filename = 'diff.html'
diff = d.make_file(text1_lines,text2_lines)
#写入html文件
with open(filename,'w') as file_object:
    file_object.write(diff)

