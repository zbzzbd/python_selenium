#-*-coding:utf-8 -*-
from PageObject.index import IndexPageObject
from models.myuntil import GangGangTestObject
from PageObject.publicObject import common_public_Gang
import unittest
class TestIndex(GangGangTestObject):
    """
    首页
    """
    def test_spot_goods(self):

        """首页去找货测试"""
        #1.登录并成功进入首页
        common_public_Gang().login_succesd(self.driver)
        #3.点击去找货
        index_pj=IndexPageObject(self.driver,'index')
        index_pj.click_spotGood_button()
        #判断是否成功调转到四方现货的页面
        index_pj.is_spod_successd()

    def test_apply_ticket(self):

        """ 申请钢票贷"""
        common_public_Gang().login_succesd(self.driver)
        #点击申请钢票贷
        index_pj = IndexPageObject(self.driver)
        index_pj.click_apply_ticket()
        index_pj.is_apply_ticket_successd()

    def test_into_mycenter(self):

        """进入个人中心测试"""
        common_public_Gang().login_succesd(self.driver)
        index_pj = IndexPageObject(self.driver)
        index_pj.click_into_my_center()
        index_pj.is_into_mycenter_succesd()

    def test_gang_newsflash(self):

        """钢钢快报"""
        #进入首页
        common_public_Gang().login_succesd(self.driver)
        #点击快报链接
        index_pj = IndexPageObject(self.driver)
        index_pj.click_and_verfity_newflashes()
        #验证是否成功进入该页面



if __name__ == "__main__":
    unittest.main()