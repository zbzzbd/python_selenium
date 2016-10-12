# -*- coding:utf-8 -*-
from until.Constant import  Constant
from base import GG_BasePage
import unittest



"""
本文件主要封装，页面的元素定位封装，登录方法的封装，检查点的封装
"""
class loginPageObject(GG_BasePage):

    def __init__(self,driver,baseurl,module_item):
        self.base_url='http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://www.ggang.cn/'+baseurl
        self.driver=driver
        self.get_elements_position(module_item)
        self.open(self.base_url)

    # 获取页面定位
    def get_elements_position(self,module_item):

        item =self.Read_elements_item(module_item)
        self.username = item.get('username')
        self.pasword = item.get('passw')
        self.logtn = item.get('submit')
        self.qiehuan = item.get('company_login_li')
        self.nameAdmin=item.get('company_login_username')
        self.passAdmin=item.get('company_login_password')
        self.logout=item.get('index_logout')
        print self.logout


    #输入用户名
    def type_username(self,username):
        find_type,value=self.get_type_locator(self.username)
        self.according_type_find_element(self.driver,find_type,value).send_keys(username)
    #输入企业用户名
    def type_company_username(self,username):
        find_type ,value =self.get_type_locator(self.nameAdmin)
        self.according_type_find_element(self.driver,find_type,value).send_keys(username)

    #输入密码
    def type_password(self,password):
        find_type, value =self.get_type_locator(self.pasword)
        self.according_type_find_element(self.driver, str(find_type), str(value)).send_keys(password)

    #输入企业密码
    def type_company_password(self,password):
        find_type, value = self.get_type_locator(self.passAdmin)
        self.according_type_find_element(self.driver, str(find_type), str(value)).send_keys(password)

    #点击登录按钮
    def click_submit(self):
        find_type, value = self.get_type_locator(self.logtn)
        self.according_type_find_element(self.driver, str(find_type), str(value)).click()


    #点击切换登录
    def click_switch_login(self):
        find_type,value = self.get_type_locator(self.qiehuan)
        self.according_type_find_element(self.driver,str(find_type),str(value)).click()

    #获取退出按钮的属性
    def get_logout_value(self):
        find_type, value = self.get_type_locator(self.logout)
        logbut=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
        text =logbut.get_attribute("value")
        return text
    #获取alter 信息
    def get_alter_info(self):
        return self.driver.switch_to_alert().text

    #判断是否成功登录（是否包含退出）
    def is_success_logined(self,text):
        if isinstance(text,unicode):
            assert text.encode("utf-8")=="退出"
        else:
            assert text=="退出"




    #登录
    def login_ganggang(self,username,passw):
        self.type_username(username)
        self.type_password(passw)
        self.click_submit()



    #企业登录
    def login_company_ganggang(self,username,passw):
        self.click_switch_login()
        self.type_company_username(username)
        self.type_company_password(passw)
        self.click_submit()



