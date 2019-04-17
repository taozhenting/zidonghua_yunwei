#!/usr/bin/python
# -*- coding: utf-8 -*-
#发送一份HTML格式的测试邮件

import smtplib
from email.mime.text import MIMEText

#定义smtp主机
HOST = "mail.gw.com.cn"
#定义邮件主题
SUBJECT = u" 官网流量数据报表 "
#定义邮件收件人
TO = "taozhenting@outlook.com"
#定义邮件发件人
FROM = "taozhenting@gw.com.cn"
#创建一个MIMEText对象，分别指定HTML内容，类型（文本或html）,字符编码
msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td bgcolor="#CECFAD" height="20" style="font-size:14px">* 官网数据 <a href="www.gw.com.cn"> 更多 >></a></td>
        </tr>
        <tr>
            <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1) 日访问量:<font color=red>908790809</font>  访问次数:23651 页面浏览量:45123 点击数:545122 数据流量:504Mb<br>
            2) 状态码信息<br>
            &nbsp;&nbsp;500:105  404:3264  503:214<br>
            3) 访客浏览器信息<br>
            &nbsp;&nbsp;IE:50%  firefox:10%  chrome:30%  other:10%<br>
            4) 页面信息<br>
            &nbsp;&nbsp;/index.php 42153<br>
            &nbsp;&nbsp;/view.php 21451<br>
            &nbsp;&nbsp;/login.php 5112<br>
            </td>
        </tr>
    </table>""","html","utf-8")

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