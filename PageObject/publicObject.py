#-*- coding:utf-8 -*-
from login import loginPageObject
from index import  IndexPageObject
from until.Constant import Constant
class common_public_Gang(object):
    """
    本文件主要存放一些公共的方法对象：比如成功登录方法的封装
    这里不同于单个对象封装这里包含了断言
    """
    def __init__(self):
        self.login_user= self.get_account().get('login_user')
        self.password= self.get_account().get('password')

    def get_account(self):
        return Constant().Read_file_config('accout')

    #企业用户成功登录
    def login_succesd(self,driver):
        p = loginPageObject(driver,'','login')
        p.login_company_ganggang(self.login_user,self.password)
        text = p.get_logout_value()
        p.is_success_logined(text)

    #进入个人中心
    def go_to_mycenter(self,driver):
        self.login_succesd(driver)
        index_pj=IndexPageObject(driver)
        index_pj.click_into_my_center()
        index_pj.is_into_mycenter_succesd()

