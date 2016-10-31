#-*- coding:utf-8 -*-
from models.myuntil import GangGangTestObject
from PageObject.publicObject import common_public_Gang
from PageObject.apllyAcount import ApplyAcountPageObjdect
class TestMyCenterApplyAccount(GangGangTestObject):
    """
    个人中心，申请企业账号
    """
    def test_apply_account(self):

        """
        申请企业账号
        """
        #1.登录进入首页并进入个人中心
        common_public_Gang().go_to_mycenter(self.driver)

        #2.点击申请企业账号
        mycenter_object = ApplyAcountPageObjdect(self.driver)
        mycenter_object.click_applyAcoount_link()
        mycenter_object.is_succesd_applyPage("申请企业账号")
