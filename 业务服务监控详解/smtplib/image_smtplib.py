#!/usr/bin/python
# -*- coding: utf-8 -*-
#发送一份HTML带图片格式的测试邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#定义smtp主机
HOST = "mail.gw.com.cn"
#定义邮件主题
SUBJECT = u" 业务性能数据报表 "
#定义邮件收件人
TO = "taozhenting@outlook.com"
#定义邮件发件人
FROM = "taozhenting@gw.com.cn"

#添加图片函数，参数1：图片路径，参数2：图片id
def addimg(src,imgid):
    #打开文件
    fp = open(src,'rb')
    #创建MIMEImage对象，采用related定义内嵌资源的邮件体
    msgImage = MIMEImage(fp.read())
    #关闭文件
    fp.close()
    #指定图片文件的Content-ID,<img>标签src用到
    msgImage.add_header('Content-ID',imgid)
    #返回msgImage对象
    return msgImage

#创建MIMEM对象
msg = MIMEMultipart('related')