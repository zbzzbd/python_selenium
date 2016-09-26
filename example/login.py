# -*- coding:utf-8 -*-

from selenium import  webdriver
from  PageObject.login import loginPageObject
from  until.Constant import Constant
import unittest


class Testlogin(unittest.TestCase):

    url='http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://www.ggang.cn/'
    def setUp(self):
        self.driver =webdriver.Firefox()

    """
    原始的缺点： 代码量多，地址变化修改，需要改动脚本，输入数据变化，需要改动脚本，定位方式变化需要改动脚本
    """
    def test_login(self):
         loginPageObject().login_ganggang(self.driver,'13611873856','123456')
    def test_login2(self):
        loginPageObject().login_ganggang(self.driver,'13611873856', '123456')

    def tearDown(self):
        Constant().close_current_window(self.driver)



if __name__ =="__main__":
   unittest.main()