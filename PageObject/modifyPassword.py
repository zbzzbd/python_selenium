# -*- coding:utf-8 -*-
from .base import GG_BasePage

class  ModifyPasswordPageObjdect(GG_BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.item=self._get_elements_position('mycenter_modify_password')


    def _get_elements_position(self,module):
        item= self.Read_elements_item(module)
        self.password_link=item.get('modify_password_link')
        self.old_password =item.get('modify_old_password')
        self.new_password = item.get('modify_new_password')
        self.confirm
    #点击修改密码链接
    def click_modify_password_link(self):
        find_type,value= self.get_type_locator(self.password_link)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()

    #输入原密码
    def input_old_password(self,oldpassword):
         self.input_text(self.old_password,oldpassword)

    #输入新密码
    def input_new_password(self,newpassword):
        self.input_text(self.new_password,newpassword)

    def input_confirm_new_password(self,confirmpassword):

        self.input_text(self.)

    def input_text(self,locator,text):
        element= self.find_element_by_locator(locator)
        element.clear()
        element.senkeys(text)



    #判断是否成功进入修改密码界面
    def is_success_load_mofiypwdPage(self,text):
        if not self.page_should_be_contain_text(text):
            raise AssertionError("没有成进入修改密码界面")
        print "成功进入修改密码界面"





