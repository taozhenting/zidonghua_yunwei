#!/usr/bin/python
# -*- coding: utf-8 -*-

#使用unicode编码
from __future__ import unicode_literals
import 系统批量运维管理器.pexpect
import sys

#运行ftp命令
child = 系统批量运维管理器.pexpect.spawnu('ftp 127.0.0.1')
#(?i)表示后面的字符串正则匹配忽略大小写
child.expect('(?i)name .*: ')
#输入ftp账号信息
child.sendline('taozhenting')
#匹配密码输入提示
child.expect('(?i)password')
#输入ftp密码
child.sendline('w59nHD!kt')
child.expect('ftp> ')
#启用二进制传输模式
child.sendline('bin')
child.expect('ftp> ')
#下载test.txt文件
child.sendline('get test.txt')
child.expect('ftp> ')
#输出匹配"ftp> "之前的输入与输出
sys.stdout.write(child.before)
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
#调用interact()让出控制权，用户可以继续当前的会话手工控制子程序，默认输入"^]"字符跳出
child.interact()
child.sendline('bye')
child.close()