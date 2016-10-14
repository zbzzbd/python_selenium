# -*- coding:utf-8 -*-
from .base import GG_BasePage
class IndexPageObject(GG_BasePage):
    def __init__(self,driver):
        self.driver=driver
        self.item=self._get_elements_position('index')

    def _get_elements_position(self,module_item):
        item =self.Read_elements_item(module_item)
        self.spot_good=item.get('spot_goods')
        self.ticket =item.get('apply_tikcet')
        self.mycenter=item.get('mycenter')
        return item
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
    #点击钢钢快报链接
    def click_and_verfity_newflashes(self):
        #获取定位方式
        for i in range(1,6):
            link=self.item.get("index_newfishs"+str(i))
            find_type,value =self.get_type_locator(link)
            link_element=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
            # 点击并获取其属性href
            link_href=link_element.get_attribute('href')
            link_text=link_element.text
            print link_href,link_text
            self.is_goto_newPage(link_href,link_text)

        #关闭窗口
        #回到主窗口

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
    #封装验证链接是否进入的相应的页面
    def is_goto_newPage(self,href_link,text):
        #1.当前URL与调转地址相同
        #2.title 包含文字内容
        self.switch_window()
        print self.driver.title
        """
        title= self.driver.title
        url= self.driver.current_url
        print title,url
        assert title.startswith(text)
        self.driver.close()
        """

