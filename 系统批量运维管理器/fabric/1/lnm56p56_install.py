#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric.colors import *
from fabric.api import *

env.user = 'root'
ldir = "/usr/local/src/"
rdir = "/usr/local/src/"

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
        run("yum -y install gcc make apr-devel apr-util-devel pcre-devel libxml2-devel curl-devel gd-devel openssl-devel autoconf libjpeg-devel libpng-devel libxslt-devel")
        run("chkconfig nginx on")
        put(ldir + "php/php-5.6.38.tar.gz", rdir + "php-5.6.38.tar.gz")
        with cd(rdir):
            run("tar zxvf php-5.6.38.tar.gz")
            with cd("php-5.6.38"):
                run("./configure \
                    --prefix=/opt/php5.6.38 \
                    --with-curl \
                    --with-freetype-dir \
                    --with-gd \
                    --with-gettext \
                    --with-iconv-dir \
                    --with-kerberos \
                    --with-libdir=lib64 \
                    --with-libxml-dir \
                    --with-mysqli \
                    --with-openssl \
                    --with-pcre-regex \
                    --with-pdo-mysql \
                    --with-pdo-sqlite \
                    --with-pear \
                    --with-png-dir \
                    --with-xmlrpc \
                    --with-xsl \
                    --with-zlib \
                    --enable-fpm \
                    --enable-bcmath \
                    --enable-libxml \
                    --enable-inline-optimization \
                    --enable-gd-native-ttf \
                    --enable-mbregex \
                    --enable-mbstring \
                    --enable-opcache \
                    --enable-pcntl \
                    --enable-shmop \
                    --enable-soap \
                    --enable-sockets \
                    --enable-sysvsem \
                    --enable-xml \
                    --enable-zip \
                    --with-jpeg-dir")
                run("make && make install")
        put(ldir + "php/php.ini", "/opt/php5.6.38/lib/php.ini")
        put(ldir + "php/php-fpm.conf", "/opt/php5.6.38/etc/php-fpm.conf")
        run("mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak")
        put(ldir + "php/nginx.conf", "/etc/nginx/nginx.conf")
        put(ldir + "php/test.php", "/usr/share/nginx/html/test.php")
        run("cp /usr/local/src/php-5.6.38/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm")
        run("chmod +x /etc/init.d/php-fpm")
        run("chkconfig --add php-fpm")
        run("chkconfig php-fpm on")
        run("systemctl start nginx")
        run("systemctl enable nginx")
        run("/etc/init.d/php-fpm start")

#dbtask任务函数引用'dbservers'角色修饰符
@roles('dbservers')
#部署mysql环境
def dbtask():
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig mysqld on")

#publictask任务函数同时引用两个角色修饰符
@roles('webservers')
#部署公共类环境，如epel，ntp等
def publictask():
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("yum -y install epel-release")
        run("yum -y install ntp")
        with cd(ldir):
            put(ldir + "mysql57-community-release-el7-11.noarch.rpm", rdir + "mysql57-community-release-el7-11.noarch.rpm")
            run("rpm -ivh mysql57-community-release-el7-11.noarch.rpm")
            put(ldir + "mysql-community.repo", "/etc/yum.repos.d/mysql-community.repo")
            run("echo \"* soft nofile 1024000\" >> /etc/security/limits.conf")
            run("echo \"* hard nofile 1024000\" >> /etc/security/limits.conf")
            run("echo \"* soft noproc 1024000\" >> /etc/security/limits.conf")
            run("echo \"* hard noproc 1024000\" >> /etc/security/limits.conf")
            run("systemctl stop firewalld.service")
            run("systemctl disable firewalld.service")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)