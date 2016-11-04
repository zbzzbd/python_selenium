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
        self.confirm_password= item.get('modify_confirm_password')
        self.submit_button = item.get('modify_submit')
        self.canel_button = item.get('modify_canel')

    #点击修改密码链接
    def click_modify_password_link(self):
        self._click_element(self.password_link)

    #输入原密码
    def input_old_password(self,oldpassword):
         self._input_text(self.old_password,oldpassword)

    #输入新密码
    def input_new_password(self,newpassword):
        self._input_text(self.new_password,newpassword)

    def input_confirm_new_password(self,confirmpassword):

        self._input_text(self.confirm_password,confirmpassword)

    #点击确认按钮
    def click_submit_button(self):
        self._click_element(self.submit_button)

    #点击取消按钮
    def click_cancel_button(self):
         self._click_element(self.canel_button)

    #修改密码
    def modify_password(self,oldpassword,newpassword,confirmpassword):

        self.input_old_password(oldpassword)
        self.input_new_password(newpassword)
        self.input_confirm_new_password(confirmpassword)



    #判断是否成功进入修改密码界面
    def is_success_load_mofiypwdPage(self,text):
        if not self.page_should_be_contain_text(text):
            raise AssertionError("没有成进入修改密码界面")
        print "成功进入修改密码界面"





