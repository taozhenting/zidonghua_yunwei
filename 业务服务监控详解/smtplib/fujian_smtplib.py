#!/usr/bin/python
# -*- coding: utf-8 -*-
#发送一份HTML带图片格式和附件的测试邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#定义smtp主机
HOST = "mail.gw.com.cn"
#定义邮件主题
SUBJECT = u" 官网业务服务质量周报 "
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

#创建一个MIMEText对象，HTML元素包括文字与图片<img>
msgtext = MIMEText("<font color=red> 官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br> 详细内容见附件。 </font>","html","utf-8")
#MIMEMultipart对象附加MIMEText的内容
msg.attach(msgtext)
#使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/weekly.png","weekly"))

#创建一个MIMEText对象，附加week_report.xlsx文档
attach = MIMEText(open("doc/week_report.xls","rb").read(),"base64","utf-8")
#指定文件格式类型
attach["Content-Type"] = "application/octet-stream"
#指定Content-Disposition值为attachment则出现下载保存对话框，保存的默认文件名使用filename指定
#由于qqmail使用gb18030页面编码，为保证中文文件名不出现乱码，对文件名进行编码转换
#attach["Content-Disposition"] = "attachment; filename=\" 业务服务质量周报(12周).xls\"".decode("utf-8").encode("gb18030")
attach["Content-Disposition"] = "attachment; filename=\" 业务服务质量周报(12周).xls\""

#MIMEMultipart对象附加MIMEText附件内容
msg.attach(attach)
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