# -*- coding:utf-8 -*-
from until.Constant import  Constant
from base import GG_BasePage


"""
本文件主要封装，页面的元素定位封装，登录方法的封装，检查点的封装
"""
class loginPageObject(GG_BasePage):

    def __init__(self):
        self.url='http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://www.ggang.cn/'
        # 读取配置文件
        self.username ,self.pasword,self.logtn= Constant().Read_file_init()

    #输入用户名
    def login_username(self,username):
        find_type, value= Constant().pase_element_find_method(self.username)
        self.according_type_find_element(self.driver,str(find_type),str(value)).send_keys(username)

    #输入密码
    def login_password(self,password):
        find_type, value = Constant().pase_element_find_method(self.pasword)
        self.according_type_find_element(self.driver, str(find_type), str(value)).send_keys(password)

    #点击登录按钮
    def login_submit(self):
        find_type, value = Constant().pase_element_find_method(self.logtn)
        self.according_type_find_element(self.driver, str(find_type), str(value)).click()



    def login_ganggang(self,driver,username,passw):

        Constant().open_url(driver,self.url)

        #获取定位方式及定位值
        username_specator, username_value = Constant().pase_element_find_method(username1)
        passw_spcator, passw_value = Constant().pase_element_find_method(passw2)
        logbutn_specator,logn_value= Constant().pase_element_find_method(logbutn)

        # 需要传入的值，定位方式，定位值，输入内容，输入值
        #输入用户名
        phone =self.according_type_find_element(driver,str(username_specator),str(username_value))
        phone.send_keys(username)
        #输入密码
        password =self.according_type_find_element(driver,str(passw_spcator),str(passw_value))
        password.send_keys(passw)

        #Constant().according_type_find_element(driver,str(logbutn_specator),str(logn_value)).click()



