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

#创建MIMEM对象,采用related定义内嵌资源的邮件体
msg = MIMEMultipart('related')

#创建一个MIMEText对象，HTML元素包括表格<table>及图片<img>
msgtext = MIMEText("""
    <table width="600" border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td bgcolor="#CECFAD" height="20" style="font-size:14px">
            <td colspan=2>* 官网性能数据 <a href="www.gw.com.cn"> 更多 >></a></td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:bytes_io"></td><td>
                <img src="cid:ms_io"></td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:mem"></td><td>
                <img src="cid:swap"></td>
        </tr>
    </table>""","html","utf-8") #<img>标签的src属性是通过Content-ID来引用的

#MIMEMultipart对象附加MIMEText的内容
msg.attach(msgtext)
#使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/bytes_io.png","bytes_io"))
msg.attach(addimg("img/ms_io.png","ms_io"))
msg.attach(addimg("img/os_mem.png","mem"))
msg.attach(addimg("img/os_swap.png","swap"))
#邮件主题
msg['Subject'] = SUBJECT
#邮件发件人，邮件头部可见
msg['From'] = FROM
#邮件收件人，邮件头部可见
msg['To'] = TO

try:
    # 创建一个SMTP()对象
    server = smtplib.SMTP()
    # 通过connect方法连接smtp主机
    server.connect(HOST, "25")
    # 启动安全传输模式
    # server.starttls()
    # 邮箱账号登录校验
    server.login("taozhenting", "wgdzh20190408")
    # 邮件发送
    server.sendmail(FROM, TO, msg.as_string())
    # 断开smtp连接
    server.quit()
    print "邮件发送成功！"
except Exception,e:
    print "失败: " + str(e)