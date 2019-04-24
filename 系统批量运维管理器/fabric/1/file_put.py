#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import sys

env.user = 'root'
#env.hosts = ['192.168.1.21','192.168.1.22']
env.hosts = ['47.102.126.128:12752','47.102.126.128:12753']
#env.port = 12752
#env.password = 'mypassword'

@task
@runs_once
#本地打包任务函数，只限执行一次
def tar_task():
    with lcd("/var/log/nginx"):
        with settings(warn_only=True):
            local("rm -f m.txread.net.access.log.tar.gz")
            local("tar czf m.txread.net.access.log.tar.gz m.txread.net.access.log")

@task
#上传文件任务函数
def put_task():
    run("mkdir -p /tmp/test")
    with cd("/tmp/test"):
        #put(上传)出现异常时继续执行，非终止
        with settings(warn_only=True):
            result = put("/var/log/nginx/m.txread.net.access.log.tar.gz","/tmp/test/m.txread.net.access.log.tar.gz")
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):
            #出现异常时，确认用户是否继续（Y继续）
            abort("Aborting file put task!")

@task
#校验文件任务函数
def check_task():
    with settings(warn_only=True):
        #本地local命令需要配置capture=True才能捕获返回值
        lmd5 = local("md5sum /var/log/nginx/m.txread.net.access.log.tar.gz",capture=True).split(' ')[0]
        rmd5 = run("md5sum /tmp/test/m.txread.net.access.log.tar.gz").split(' ')[0]
    if lmd5 == rmd5:
        print "OK"
    else:
        print "ERROR"
        sys.exit()

@task
@runs_once
#删除本地压缩文件
def rm_task():
    with lcd("/var/log/nginx"):
        local("rm -f m.txread.net.access.log.tar.gz")

@task
#解压远程文件
def un_task():
    with cd("/tmp/test"):
        run("tar zxf m.txread.net.access.log.tar.gz")
        run("rm -f m.txread.net.access.log.tar.gz")


@task
#批量运行
def go():
    tar_task()
    put_task()
    check_task()
    un_task()