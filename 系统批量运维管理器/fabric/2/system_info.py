#!/usr/bin/python
# -*- coding: utf-8 -*-

from fabric import Connection

c = Connection('47.102.126.128', port=12752, user='root')
c.run('uname -a')
