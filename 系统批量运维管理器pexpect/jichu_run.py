#!/usr/bin/python
# -*- coding: utf-8 -*-

""""
import pexpect

child = pexpect.spawn('scp foo user@example.com:.')
child.expect('(?i)password')
child.sendline(mypassword)

#使用run函数实现如下
pexpect.run('scp foo user@example.com:.', events = {'(?i)password': mypassword})
"""