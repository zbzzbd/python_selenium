# -*-coding:utf-8 -*-
from models.myuntil import GangGangTestObject
import unittest
from PageObject.publicObject import common_public_Gang

from PageObject.modifyPassword import ModifyPasswordPageObjdect
class TestModifyPassword(GangGangTestObject):

    def setUp(self):
        GangGangTestObject.setUp(self)
        common_public_Gang().go_to_mycenter(self.driver)
        self.pass_obj = ModifyPasswordPageObjdect(self.driver)

    def test_modify_password_link(self):
        """进入修改密码"""

        self.pass_obj.click_modify_password_link()
        self.pass_obj.is_success_load_mofiypwdPage("原密码")

    def test_modify_password(self):

        """修改密码"""
        self.pass_obj.click_modify_password_link()
        self.pass_obj.is_success_load_mofiypwdPage("原密码")
        self.pass_obj.modify_password('123456','123456','123456')




if __name__=='__main__':
    unittest.main()
