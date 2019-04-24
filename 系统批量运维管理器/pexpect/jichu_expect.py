#!/usr/bin/python
# -*- coding: utf-8 -*-

import pexpect
import sys

#参数pattern表示字符串，pexpect.EOF(指向缓冲区尾部，无匹配项），pexpect.TIMEOUT(匹配等待超时)，单位为秒；参数searchwindowsize为匹配缓冲区字符串的位置，默认从开始位置匹配
#pexpect(pattern,timeout=-1,searchwindowsize=-1)

#当patten为一个列表时，且不知一个表列元素被匹配，则返回结果是输出最先那个元素或是列表最左边的元素(最小索引ID)
child = pexpect.spawn("echo 'foobar'")
#输出1，即'foo'被匹配
print child.expect(['bar', 'foo', 'foobar'])

#当pexpect.EOF,pexpect.TIMEOUT作为expect的列表参数时，匹配时将返回所处列表中的索引ID
"""
index = p.pexpect(['good', 'bad', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    do_something()
elif index == 1:
    do_something_else()
elif index == 2:
    do_some_other_thing()
elif index == 3:
    do_something_completely_different()
"""
#以上代码等价于：
"""
try:
    index = p.pexpect(['good', 'bad'])
    if index == 0:
        do_something()
    elif index == 1:
        do_something_else()
except EOF:
    do_some_other_thing()
except TIMEOUT:
    do_something_completely_different()
"""

#before成员保存了最近匹配成功之前的内容，after保存了最近匹配成功之后的内容
child = pexpect.spawn('ssh -p 12752 root@47.102.126.128')
fout = file('mylog.txt','w')
child.logfile = fout

child.expect('#')
child.sendline('ls /home')
child.expect('\[root@jinju-manhua-test ~\]#')
fout.close()
print "before:" + child.before
print "after:" + child.after

#下面输入方法的作用是向子程序发送响应命令，可以理解成代替了我们的标准输入键盘
"""
send(self, s) 发送命令，不回车
sendline(self, s='') 发送命令，回车
sendcontrol(self, char) 发送控制字符，如child.sendcontrol('c')等价于"crtl + c"
sendeof() 发送eof
"""