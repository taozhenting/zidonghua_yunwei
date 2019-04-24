#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os

hostname = '47.102.126.128'
port=int('12752')
username = 'root'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
#定义私钥存放路径
#privatekey = os.path.expanduser('/home/key/id_rsa')
#key = paramiko.RSAKey.from_private_key_file(privatekey)

#ssh.connect(hostname=hostname,port=port,username=username,pkey=key)
ssh.connect(hostname=hostname,port=port,username=username)
stdin,stdout,stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()