#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pexpect

#参数timeout为等待结果的超时时间；参数maxread为pexpect从终端控制台一次读取的最大字节数，searchwindowsize参数为匹配缓冲区字符串的位置，默认是从开始位置匹配
#class pexpect.spawn(command, args = [], timeout = 30, maxread = 2000, searchwindowsize = None, logfile = None, cwd = None, env = None, ignore_sighup = True)

#运行ls显示/tmp目录内容命令
child = pexpect.spawn('ls -latr /tmp')
#内容输出到屏幕
child.logfile = sys.stdout
child.expect(pexpect.EOF)

child = pexpect.spawn('ls -latr /tmp')
#内容输出到文件
fout = file('./mylog.txt','w')
child.logfile = fout
child.expect(pexpect.EOF)
fout.close()

#当子程序需要参数时，还可以使用Python列表来代替参数项
child = pexpect.spawn('ls', ['-latr', '/tmp'])
child.expect(pexpect.EOF)

#支持三个元字符（重定向>，管道|，通配符*
child = pexpect.spawn('/bin/bash -c "ls -l /tmp | grep LOG > logs.txt"')
child.expect(pexpect.EOF)

#支持三个元字符（重定向>，管道|，通配符*，列表方式写法，推荐
shell_cmd = 'ls -l /tmp | grep LOG > logs.txt'
child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
child.expect(pexpect.EOF)
