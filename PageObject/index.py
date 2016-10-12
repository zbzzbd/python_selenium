# -*- coding:utf-8 -*-
from .base import GG_BasePage
class IndexPageObject(GG_BasePage):
    def __init__(self,driver,module_item):
        self.driver=driver
        self._get_elements_position(module_item)

    def _get_elements_position(self,module_item):
        item =self.Read_elements_item(module_item)
        self.spot_good=item.get('spot_goods')

    #点击去找货
    def click_spotGood_button(self):
        find_type,value = self.get_type_locator(self.spot_good)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()


    #封装验证找货的正确
    def is_spod_successd(self):
        #1.转化窗口
        self.switch_window()


