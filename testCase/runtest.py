#-*- coding:utf-8 -*-
import unittest
import os
import time
import test_login
from HTMLTestRunner import HTMLTestRunner
from models.function import *
#构造测试集

if __name__ == "__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(login.Testlogin("test_login"))

    #指定测试用例为当前文件夹下的路径
    test_dir=os.path.dirname(os.path.abspath(__file__))
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    # 定义报告输出路径
    ReportDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\report\\"
    print ReportDir
    now =time.strftime("%Y-%m-%d %H_%M_%S")
    fp =open(ReportDir+now+'result.html','wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    #运行用例

    runner.run(discover)
    fp.close()

    #查找最新报告并邮件发送
    #new_report=new_report(ReportDir)
    #send_mail(new_report)
