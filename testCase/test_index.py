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
        """
        首页去找货测试
        """
        #1.登录并成功进入首页
        common_public_Gang().login_succesd(self.driver,'','login')
        #3.点击去找货
        index_pj=IndexPageObject(self.driver,'index')
        index_pj.click_spotGood_button()
        #判断是否成功调转到四方现货的页面
        index_pj.is_spod_successd()


if __name__ == "__main__":
    unittest.main()