#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.api import *


env.user = 'root'
env.hosts = ['47.102.126.128:12752','47.102.126.128:12753']
#env.port = 12752
#env.password = 'mypassword'

#查看本地系统信息，当有多台主机时只允许一次
@runs_once
def local_task():
    local("ifconfig")

def remote_task():
    #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /home && ls -l"的效果
    with cd("/home"):
        run("ls -l")