#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.colors import *
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import *
import time

env.user = 'root'
env.hosts = ['192.168.239.11','192.168.239.12']
#env.password = 'mypassword'

#开发机项目主目录
env.project_dev_source = '/data/dev/webadmin/'
#开发机项目压缩包存储目录
env.project_tar_source = '/data/dev/releases/'
#项目压缩包名前缀，文件名为'release.tar.gz'
env.project_pack_name = 'release'

#项目生产环境主目录
env.deploy_project_root = '/usr/share/nginx/html/testweb/'
#项目发布目录，位于主目录下面
env.deploy_release_dir = 'releases'
#对外服务的当前版本软连接
env.deploy_current_dir = 'current'
#版本号
#env.deploy_version = time.strftime("%Y%m%d")

@runs_once
def input_vid():
    vid = raw_input("Please input the deployment version ID:")
    if vid == '':
        abort("Project version ID error,abort!")
    env.deploy_version = time.strftime("%Y%m%d") + vid
#获得用户输入的版本号，以便做版本回滚操作
def input_versionid():
    versionid = raw_input("Please input profect rollback version ID:")
    if versionid == '':
        abort("Project version ID error,abort!")
    env.versionid = versionid
@task
@runs_once
#打包本地项目主目录，并将压缩包存储到本地压缩包目录
def tar_source():
    print yellow("Creating source package...")
    with lcd(env.project_dev_source):
        local("tar cvzf %s.tar.gz ." % (env.project_tar_source + env.project_pack_name))
    print green("Creating source package success!")

@task
#上传任务函数
def put_package():
    print yellow("Start put package...")
    with settings(warn_only = True):
        with cd(env.deploy_project_root + env.deploy_release_dir):
            #创建版本目录
            run("mkdir %s" % (env.deploy_version))
        env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version
        with settings(warn_only = True):
            result = put(env.project_tar_source + env.project_pack_name + ".tar.gz", env.deploy_full_path)
        if result.failed and not("put file failed, Continue[Y/N]?"):
            abort("Aborting file put task!")

        #成功解压后删除压缩包
        with cd(env.deploy_full_path):
            run("tar -zxvf %s.tar.gz" % (env.project_pack_name))
            run("rm -f %s.tar.gz" % (env.project_pack_name))

        print green("Put & untar package success!")

@task
#为当前版本目录做软连接
def make_symlink():
    print yellow("update current symlink")
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version
    #删除软连接，重新创建并指定软连接源目录，新版本生效
    with settings(warn_only = True):
        run("rm -rf %s" % (env.deploy_project_root + env.deploy_current_dir))
        run("ln -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
    print green("make symlink success!")

@task
#版本回滚任务函数
def roll_back():
    print yellow("rollback project version")
    #获得用户输入的回滚版本号
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.versionid
    run("rm -f %s" % env.deploy_project_root + env.deploy_current_dir)
    #删除软连接，重新创建并指定软连接目录，新版本生效
    run("ln -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
    print green("rollback success!")

@task
#自动化程序版本发布入口函数
def go():
    input_vid()
    tar_source()
    put_package()
    make_symlink()

def rollback():
    input_versionid()
    roll_back()