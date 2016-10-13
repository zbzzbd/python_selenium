# -*- coding:utf-8 -*-
from .base import GG_BasePage
class IndexPageObject(GG_BasePage):
    def __init__(self,driver,module_item):
        self.driver=driver
        self._get_elements_position(module_item)

    def _get_elements_position(self,module_item):
        item =self.Read_elements_item(module_item)
        self.spot_good=item.get('spot_goods')
        self.ticket =item.get('apply_tikcet')
        self.mycenter=item.get('mycenter')

    #点击去找货
    def click_spotGood_button(self):
        find_type,value = self.get_type_locator(self.spot_good)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()
    #点击申请钢票贷
    def click_apply_ticket(self):
        find_type,value = self.get_type_locator(self.ticket)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()

    # 点击我的钢钢网
    def click_into_my_center(self):
        find_type,value=self.get_type_locator(self.mycenter)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()


    #封装验证是否成功跳入四方现货页面
    def is_spod_successd(self):
        #1.转化窗口
        self.switch_window()
        #获取窗口标题
        title = self.driver.title
        assert  title.encode("utf-8").startswith('钢钢网-四方现货')
    #封装是否成功跳入钢钢网页面
    def is_apply_ticket_successd(self):
        self.switch_window()
        title = self.driver.title
        assert  title.encode("utf-8").startswith('钢钢网-大象钢票')

    #封装是否成功进入个人中心
    def is_into_mycenter_succesd(self):
        self.switch_window()
        title = self.driver.title
        assert  title.encode("utf-8").startswith('钢钢网-会员中心')
