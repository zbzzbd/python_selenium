# -*- coding:utf-8 -*-

from selenium import  webdriver
from  PageObject.login import loginPageObject
from  until.Constant import Constant
import unittest
from models.myuntil import GangGangTestObject


class Testlogin(GangGangTestObject):
    """
    原始的缺点： 代码量多，地址变化修改，需要改动脚本，输入数据变化，需要改动脚本，定位方式变化需要改动脚本
    """
    def test_login(self):
         loginPageObject().login_ganggang(self.driver,'13611873856','123456')
    def test_login2(self):
        loginPageObject().login_ganggang(self.driver,'13918739640', '123456')




if __name__ =="__main__":
   unittest.main()