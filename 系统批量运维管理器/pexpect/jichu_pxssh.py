#!/usr/bin/python
# -*- coding: utf-8 -*-

from 系统批量运维管理器.pexpect import pxssh
import getpass

try:
    #创建pxssh对象s
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    port = raw_input('ssh_port:')
    username = raw_input('username: ')
    #接受密码输入
    password = getpass.getpass('please input password: ')
    #建立ssh连接
    s.login(hostname,username,password,port=port)
    #运行uptime命令
    s.sendline('uptime')
    #匹配系统提示符
    s.prompt()
    #打印出现系统提示符前的命令输出
    print s.before
    s.sendline('ls -l')
    s.prompt()
    print s.before
    s.sendline('df')
    s.prompt()
    print s.before
    #断开ssh连接
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)