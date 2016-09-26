# -*- coding:utf-8 -*-
from until.Constant import  Constant

class loginPageObject(object):

    def __init__(self):
        self.url='http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://www.ggang.cn/'


    def login_ganggang(self,driver,username,passw):

        Constant().open_url(driver,self.url)
        #读取配置文件
        username1,passw2,logbutn=Constant().Read_file_init()
        #获取定位方式及定位值
        username_specator, username_value = Constant().pase_element_find_method(username1)
        passw_spcator, passw_value = Constant().pase_element_find_method(passw2)
        logbutn_specator,logn_value= Constant().pase_element_find_method(logbutn)

        # 需要传入的值，定位方式，定位值，输入内容，输入值
        #输入用户名
        phone =Constant().according_type_find_element(driver,str(username_specator),str(username_value))
        phone.send_keys(username)
        #输入密码
        password =Constant().according_type_find_element(driver,str(passw_spcator),str(passw_value))
        password.send_keys(passw)

        Constant().according_type_find_element(driver,str(logbutn_specator),str(logn_value)).click()


