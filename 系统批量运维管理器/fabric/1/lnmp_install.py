#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.colors import *
from fabric.api import *

env.user = 'root'
#定义业务角色分组
env.roledefs = {
    'webservers': ['192.168.239.11', '192.168.239.12'],
    'dbservers': ['192.168.239.11']
}

"""
env.passwords = {
    'root@192.168.239.11:22': 'mypassword',
    'root@192.168.239.12:22': 'mypassword'
}
"""

#webtask任务函数引用'webservers'角色修饰符
@roles('webservers')
#部署nginx php php-fpm等环境
def webtask():
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")

#dbtask任务函数引用'dbservers'角色修饰符
@roles('dbservers')
#部署mysql环境
def dbtask():
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")

#publictask任务函数同时引用两个角色修饰符
@roles('webservers', 'dbservers')
#部署公共类环境，如epel，ntp等
def publictask():
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("yum -y install epel-release")
        run("yum -y install ntp")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)