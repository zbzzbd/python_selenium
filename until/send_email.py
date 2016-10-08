#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import  os
#发送邮件服务器

smtpserver="smtp.exmail.qq.com"

#发送邮箱用户名/密码
user="service@ggang.cn"
password="ggw@123456"
#发送邮箱
sender="service@ggang.cn"

#接收邮箱
receiver='zhangbingzhen@ggang.cn'

#发送主题
subject = 'python email test'

#编写邮件内容
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

#发送的附件
file_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\report\\"
lists = os.listdir(file_dir)
lists.sort(key=lambda fn: os.path.getmtime(file_dir+fn))
print (('最新文件为：' +lists[-1]))
file = os.path.join(file_dir,lists[-1])
print(file)

sendfile= open(file,'rb').read()

att = MIMEText(sendfile,'base64','utf-8')

att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]="attachment;filename='2016-10-08 14_54_56result.html'"
msgRoot =MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

# 链接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()