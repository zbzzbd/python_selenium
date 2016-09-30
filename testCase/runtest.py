#-*- coding:utf-8 -*-
import unittest
import login
from HTMLTestRunner import HTMLTestRunner
#构造测试集



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(login.Testlogin("test_login"))

    #定义报告输出路径
    fp =open('./result.html','wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')

    runner.run(suite)#运行用例
    fp.close()
