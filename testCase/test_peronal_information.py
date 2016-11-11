# -*- coding:utf-8 -*-
from models.myuntil import GangGangTestObject
from PageObject.personalModify import PersonalModifyInfo
from PageObject.publicObject import common_public_Gang
class TestPersonalInformation(GangGangTestObject):

    def setUp(self):
        GangGangTestObject.setUp(self)
        common_public_Gang().go_to_mycenter(self.driver)
        self.personinfo=PersonalModifyInfo(self.driver)



    def test_modify_personalInfo(self):
        self.personinfo.click_personal_info_link()
        self.personinfo.modify_personal_info("张四",'女',"钢钢网")


