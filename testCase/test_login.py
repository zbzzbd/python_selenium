# -*- coding:utf-8 -*-

from  PageObject.login import loginPageObject
import unittest
from models.myuntil import GangGangTestObject


class Testlogin(GangGangTestObject):
    """
    原始的缺点： 代码量多，地址变化修改，需要改动脚本，输入数据变化，需要改动脚本，定位方式变化需要改动脚本
    """

    def test_login(self):

        """钢钢网登录测试"""
        p=loginPageObject(self.driver, '','login')
        p.login_company_ganggang('13611873856','123456')
        text=p.get_logout_value()
        self.assertEqual(text,"退出")

        self.assertEqual()
    def test_login2(self):
        loginPageObject(self.driver, '','login').login_ganggang('13918739640', '123456')




if __name__ =="__main__":
   unittest.main()