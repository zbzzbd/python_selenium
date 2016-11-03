#-*- coding:utf-8 -*-
from models.myuntil import GangGangTestObject
from PageObject.publicObject import common_public_Gang
from PageObject.apllyAcount import ApplyAcountPageObjdect

class TestMyCenterApplyAccount(GangGangTestObject):
    """
    方法重写，setup,首先进入个人中心
    """

    def setUp(self):
        #调用父类GangGangTestObject中的setup()方法
        GangGangTestObject.setUp(self)
        # 1.登录进入首页并进入个人中心
        common_public_Gang().go_to_mycenter(self.driver)


    def test_apply_account(self):
        """
        申请企业账号
        """
        mycenter_object = ApplyAcountPageObjdect(self.driver)

        mycenter_object.click_applyAcoount_link()

        mycenter_object.is_succesd_loadPage("申请企业账号")