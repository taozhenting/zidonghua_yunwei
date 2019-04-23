#!/usr/bin/python
# -*- coding: utf-8 -*-

import pexpect
import sys

child = pexpect.spawn('ssh -p 12752 root@47.102.126.128')
fout = file('./mylog.txt','w')
child.logfile = fout
#child.logfile = sys.stdout

#使用密码不太安全，这里使用ssh免密码
#child.expect("password:")
#child.sendline("mypassword")
child.expect('#')
child.sendline('ls /home')
child.expect('#')
fout.close()
