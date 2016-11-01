#-*-coding:utf-8 -*-
from .base import GG_BasePage
from until.Constant import Constant

class ApplyAcountPageObjdect(GG_BasePage):
    def __init__(self,driver):
        self.driver=driver
        self.item=self._get_elements_position('mycenter')

    def _get_elements_position(self,module):
        item = self.Read_elements_item(module)
        self.apply_accout_link =item.get('mycenter_apply_account_link')

    #点击申请企业账号
    def click_applyAcoount_link(self):
        find_type,value = self.get_type_locator(self.apply_accout_link)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()


    #判断是否成功进入了企业申请账号页面

    def is_succesd_applyPage(self,str1):
        flage=self.page_should_be_contain_text(str1)
        print type(flage)
        if not  flage:
            raise AssertionError("页面中不包含此内容'%s'" %str1)
        print "成功进入申请账号页面"

