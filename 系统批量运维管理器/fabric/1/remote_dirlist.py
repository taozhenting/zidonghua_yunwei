#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.api import *

env.user = 'root'
#env.hosts = ['192.168.1.21','192.168.1.22']
env.hosts = ['47.102.126.128']
env.port = 12752
#env.password = 'mypassword'

#主机遍历过程中，只有第一台触发此函数
@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l " + dirname)

#限定只有go函数对fab命令可见
@task
def go():
    getdirname = input_raw()
    worktask(getdirname)

#执行方法：fab -f remote_dirlist.py go