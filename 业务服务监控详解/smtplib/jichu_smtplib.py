#!/usr/bin/python
# -*- coding: utf-8 -*-
#发送一份测试邮件

import smtplib
import string

#定义smtp主机
HOST = "mail.gw.com.cn"
#定义邮件主题
SUBJECT = "Test email from Python"
#定义邮件收件人
TO = "taozhenting@outlook.com"
#定义邮件发件人
FROM = "taozhenting@gw.com.cn"
#邮件内容
text = "Python rules them all!"
#组装sendmail方法的邮件主体内容，各段以"\r\n"进行分隔
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
)
    , "\r\n"
)

#创建一个SMTP()对象
server = smtplib.SMTP()
#通过connect方法连接smtp主机
server.connect(HOST,"25")
#启动安全传输模式
#server.starttls()
#邮箱账号登录校验
server.login("taozhenting","wgdzh20190408")
#邮件发送
server.sendmail(FROM,[TO],BODY)
#断开smtp连接
server.quit()