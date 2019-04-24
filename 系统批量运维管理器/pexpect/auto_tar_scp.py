#!/usr/bin/python
# -*- coding: utf-8 -*-

import 系统批量运维管理器.pexpect
import sys

#定义目标主机
ip = "47.102.126.128"
#目标主机用户
user = "root"
#目标端口
port = "12752"
#目标主机密码
#passwd = "mypasswd"
#目标主机nginx日志文件
target_file = "/var/log/nginx/m.txread.net.access.log"

#运行ssh命令
child = 系统批量运维管理器.pexpect.spawn('/usr/bin/ssh', ['-p ' + port , user + '@' + ip])
#输入，输出日志写入mylog.txt文件
fout = file('mylog.txt','w')
child.logfile = fout


try:
    #匹配password字符串，(?i)表示不区别大小写
    #child.pexpect('(?i)password')
    #child.sendline(passwd)
    child.expect('#')
    #打包nginx日志文件
    child.sendline('tar -cvzPf /tmp/m.txread.net.access.log.tar.gz ' + target_file)

    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
#定义EOF异常处理
except 系统批量运维管理器.pexpect.EOF:
    print "pexpect EOF"
#定义TIMEOUT异常处理
except 系统批量运维管理器.pexpect.TIMEOUT:
    print "pexpect TIMEOUT"


#启动scp远程拷贝命令，实现将打包好的nginx日志复制到本地/tmp目录
child = 系统批量运维管理器.pexpect.spawn('/usr/bin/scp', ['-P ' + port , user + '@' + ip + ':/tmp/m.txread.net.access.log.tar.gz', '/tmp'])
fout = file('mylog.txt','a')
child.logfile = fout
try:
    #child.pexpect('(?i)password')
    #child.sendline(passwd)
    #匹配缓冲区EOF(结尾)，保证文件复制正常完成
    child.expect(系统批量运维管理器.pexpect.EOF)
except 系统批量运维管理器.pexpect.EOF:
    print "pexpect EOF"
except 系统批量运维管理器.pexpect.TIMEOUT:
    print "pexpect TIMEOUT"