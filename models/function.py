# -*-coding:utf-8 -*-
"""
本函数主要撰写常用工具，比如：截图
"""
from selenium import  webdriver

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os

def insert_img(driver,filename):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    print base_dir
    base_dir = base_dir.replace('\\','/')
    print base_dir

    #base = base_dir.split('/testCase')[0]

    file_path = base_dir + "\\report\\image\\" +filename

    driver.get_screenshot_as_file(file_path)


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("钢钢网自动化测试报告", "utf-8")
    # 发送邮件服务器
    smtpserver = "smtp.exmail.qq.com"
    # 发送邮箱用户名/密码
    user = "service@ggang.cn"
    password = "ggw@123456"
    # 发送邮箱
    sender = "service@ggang.cn"
    # 接收邮箱
    receiver = 'zhangbingzhen@ggang.cn'

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print "email has send out!"


def new_report(restreport):
    lists = os.listdir(restreport)
    lists.sort(key=lambda fn: os.path.getmtime(restreport + fn))
    print (('最新文件为：' + lists[-1]))
    file = os.path.join(restreport, lists[-1])
    print(file)
    return file

if __name__ == "__main__":
    driver=webdriver.Firefox()
    driver.get("http://www.ggang.cn")
    insert_img(driver,'ggang.jpg')
    driver.quit()