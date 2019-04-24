#!/usr/bin/python
# -*- coding: utf-8 -*-

import 系统批量运维管理器.pexpect
import sys

child = 系统批量运维管理器.pexpect.spawn('ssh -p 12752 root@47.102.126.128')
fout = file('./mylog.txt','w')
child.logfile = fout
#child.logfile = sys.stdout

#使用密码不太安全，这里使用ssh免密码
#child.pexpect("password:")
#child.sendline("mypassword")
child.expect('#')
child.sendline('ls /home')
child.expect('#')
fout.close()
